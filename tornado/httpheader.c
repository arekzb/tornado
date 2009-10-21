/*
 * Copyright 2009 Arek Bochinski
 *
 * Licensed under the Apache License, Version 2.0 (the "License"); you may
 * not use this file except in compliance with the License. You may obtain
 * a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
 * WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
 * License for the specific language governing permissions and limitations
 * under the License.
 */

#include "Python.h"
#include <string.h>
#include <stdio.h>

static PyObject*
_httpheader_generate_headers(PyObject* self, PyObject* args) {
	PyObject *hArray = NULL;
	PyObject *s = NULL;
	PyObject *result = PyString_FromString("");
	s = PyString_FromString("\r\n");
	hArray = Py_BuildValue(
			"[s,s,s,s,s,s]",
			"HTTP/1.0 200 OK",
			"Content-Length: 12",
			"Etag: \"e02aa1b106d5c7c6a98def2b13005d5b84fd8dc8\"",
			"Content-Type: text/html; charset=UTF-8",
			"Server: TornadoServer/0.1",
			"\r\n");
	
	s = _PyString_Join(s, hArray);
	//result = Py_BuildValue("ss",s,"\r\n\r\n");
	PyString_ConcatAndDel(&result,s);
		
	Py_DECREF(hArray);
	
	return result;
}
/*
 * Returns a dictionary of headers parsed from passed in string.
 * {"Host" : "google.com" , "User-Agent" : "Mozilla/Firefox"}
 */
static PyObject* 
_httpheader_parse(PyObject* self, PyObject* args) {
    
	const char *data;
	int i , j , x; /* reset to zero */
	int delim = 0;
	int delim_val = 0;
	int len;
    PyObject* hDict = NULL;
    PyObject *pyname, *pyvalue;
    
    if (!PyArg_ParseTuple(args, "s", &data)) {
        return NULL;
    }
    
    hDict = PyDict_New();
    len = strlen(data);
   
	for(i = j = 0 ; i < len ; ) {
    	int eol;
    	
    	while( i < len && data[i] != '\n' && data[i] != '\r') {
			if(!x && data[i]==':'){
				delim=i;
				x=1;
			}
			if(x && (data[i]!=':' &&data[i]!=' ') && !delim_val ) {
				delim_val=i;
			}
			++i;
		}
    	
    	eol = i;
    	if( i < len ) {
    		if (data[i] == '\r' && i + 1 < len && data[i+1] == '\n')
    			i += 2;
    		else
    			++i;
    	}
		
		if(x) {
	    	pyname=PyString_FromStringAndSize(data+j, delim -j);
	    	pyvalue=PyString_FromStringAndSize(data+delim_val, eol-delim_val);
	        PyDict_SetItem(hDict,pyname,pyvalue);
	        Py_DECREF(pyname);
	        Py_DECREF(pyvalue);
		}
    	j = i;
		x=0;
		delim_val=0;
    }
        
    return hDict;
}

/*
 * Our method declararations
 */
static PyMethodDef kHttpheaderMethods[] = {
  {"httpheader_parse", _httpheader_parse, METH_VARARGS,
   "Parse string into HTTP Headers"},
   {"httpheader_generate_headers", _httpheader_generate_headers, METH_VARARGS,
   "Generate HTTP Headers"},
  {NULL, NULL, 0, NULL}
};

/*
 * Module initialization
 */
PyMODINIT_FUNC inithttpheader(void) {
    Py_InitModule("httpheader", kHttpheaderMethods);
}
