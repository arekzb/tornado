# httpheader unit test
# Distributed under BSD license
# Copyright Arek Bochinski
# You agree to retain this license notice if you want to use this software
#
#

import unittest
import httpheader
import logging
import sys

class HttpheaderUnit():
  def __init__(self):
    self.stats = {}
    self.testKey = ''
    
    self.logger = logging.getLogger('httpheader_test')
    self.logger.setLevel(logging.INFO)
    
    self.formatter = logging.Formatter("%(name)s - %(levelname)s%(message)s")
    self.sto = logging.StreamHandler(sys.stdout)
    self.sto.setLevel(logging.INFO)
    self.sto.setFormatter(self.formatter)
    
    self.logger.addHandler(self.sto)
    
    self.headers = \
    {
     "Accept: " : 
     ["text/plain","text/html","image/jpeg","text/x-dvi","text/x-c","text/*, text/html, text/html;level=1","*/*"],
     "Accept-Charset: " :
     ["iso-8859-5","iso-8859-5, unicode-1-1","iso-8859-5, unicode-1-1;q=0.8"],
     "Accept-Encoding: " :
     ["compress, gzip","","*","compress;q=0.5, gzip;q=1.0","gzip;q=1.0, identity; q=0.5, *;q=0"],
     "Accept-Language: " :
     ["en","en-gb","de, en-gb;q=0.8, en-gb;q=0.7"],
     "Accept-Ranges: " :
     ["bytes","none"],
     "Age: " :
     ["0","1","1234567890"],
     "Allow: " :
     ["GET","HEAD","PUT","POST","DELETE"],
     "Authorization: " :
     ["user username:password","kerberos parameters"],
     "Cache-Control: " :
     ["no-cache","no-store","no-transform","only-if-cached","public","must-revalidate","proxy-revalidate","private, community=\"UCI\""],
     "Connection: " :
     ["close"],
     "Content-Encoding: " :
     ["gzip","gzip,deflate"],
     "Content-Language: " :
     ["da","en, fr"],
     "Content-Length: " :
     ["0","1","1234567890"],
     "Content-Location: " :
     ["/content","/content/directory/content.html","http://content.loc/content.html","http://content.loc/content.html?k=v"],
     "Content-MD5: " :
     ["Q2hlY2sgSW50ZWdyaXR5IQ=="],
     "Content-Range: " :
     ["0-100","bytes 0-1023/1024","bytes 1022-1023/1024"],
     "Content-Type: " :
     ["text/html; charset=ISO-8859-4","text/plain"],
     "Date: " :
     ["Tue, 15 Nov 1994 08:12:31 GMT"],
     "ETag: " :
     ["qwerty","woeiruqpwoieuowqieurqwpoeiruwqoeiru","W/\"asdf\"","\"\""],
     "Expect: " :
     ["100-Continue"],
     "Expires: " :
     ["Tue, 15 Nov 1994 08:12:31 GMT"],
     "From: " :
     ["mail@mail.com"],
     "Host: " :
     ["www.domain.org"],
     "If-Match: " :
     ["a","\"a\", \"b\"", "*"],
     "If-Modified-Since: " :
     ["Sat, 29 Oct 1994 19:43:31 GMT"],
     "If-None-Match: " :
     ["a","\"a\", \"b\"", "*"],
     "If-Range: " :
     ["Sat, 29 Oct 1994 19:43:31 GMT"],
     "If-Unmodified-Since: " :
     ["Sat, 29 Oct 1994 19:43:31 GMT"],
     "Last-Modified: " :
     ["Sat, 29 Oct 1994 19:43:31 GMT"],
     "Location: " :
     ["http://domain.org"],
     "Max-Forwards: " :
     ["1","123123123123123"],
     "Pragma: " :
     ["no-cache"],
     "Proxy-Authenticate: " :
     ["Basic 1283974621987346"],
     "Proxy-Authorization: " :
     ["1283974621987346"],
     "Referer: " :
     ["/index","/","http://domain.org?k=v"],
     "Retry-After: " :
     ["Fri, 31 Dec 1999 23:59:59 GMT","3600"],
     "Server: " :
     ["Webserver","Webserver 1.1/mod/ext"],
     "TE: " :
     ["deflate","trailers, deflate;q=0.5"],
     "Transfer-Encoding: " :
     ["chunked"],
     "Upgrade: " :
     ["HTTP/2.0, SHTTP/1.3, IRC/6.9, RTA/x11"],
     "User-Agent: " :
     ["Mozilla","IE 4.1","Client 1/Version 1.1"],
     "Via: " :
     ["1.0 here, 1.1 there, (server)"],
     "WWW-Authenticate: " :
     ["Basic realm=\"server\""]
     
    }
  
  def run(self,tests):
    for test in tests:
      test()      
    return
  
  def dataTest(self):
    k=self.testKey
    v=self.headers[k]
    for hval in v:
      hdr = k+hval+"\r\n"
      tval = httpheader.httpheader_parse(hdr)
      tval_key = tval.keys()[0]
      #print k, tval_key
      if k.rstrip(": ") != tval_key:
        self.logger.warn("['%s' IS NOT EQUAL '%s'] ...key fail"%(k,tval_key))
      else:
        self.logger.info("['%s' '%s'] ...key pass"%(tval_key,tval_key))
        if hval != tval[tval_key]:
          self.logger.warn("['%s' IS NOT EQUAL '%s'] ...value fail"%(hval,tval[tval_key]))
        else:
          self.logger.info("['%s' '%s'] ...value pass"%(hval,tval[tval_key]))
          
  def testHeaderAccept(self):
    self.testKey="Accept: "
    self.dataTest()

  def testHeaderAcceptCharset(self):
    self.testKey="Accept-Charset: "
    self.dataTest()
      
  def testHeaderAcceptEncoding(self):
    self.testKey="Accept-Encoding: "
    self.dataTest()

  def testHeaderAcceptLanguage(self):
    self.testKey="Accept-Language: "
    self.dataTest()

  def testHeaderAcceptRanges(self):
    self.testKey="Accept-Ranges: "
    self.dataTest()
    
  def testHeaderAge(self):
    self.testKey="Age: "
    self.dataTest()
    
  def testHeaderAllow(self):
    self.testKey="Allow: "
    self.dataTest()
    
  def testHeaderAuthorization(self):
    self.testKey="Authorization: ";
    self.dataTest()

  def testHeaderCacheControl(self):
    self.testKey="Cache-Control: ";
    self.dataTest()
    
if __name__=='__main__':
  unit = HttpheaderUnit()
  unit.run(
           [unit.testHeaderAccept,unit.testHeaderAcceptCharset, \
            unit.testHeaderAcceptEncoding,unit.testHeaderAcceptLanguage, \
            unit.testHeaderAcceptRanges,unit.testHeaderAge, \
            unit.testHeaderAllow,unit.testHeaderAuthorization, \
            unit.testHeaderCacheControl]
           )
  #unit.testHeaderAccept()
  #unit.testHeaderAcceptCharset()
  #unit.testHeaderAcceptEncoding()