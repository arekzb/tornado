#!/bin/bash

# run ab bash script
# Licensed under BSD
# Copyright Arek Bochinski
# You agree to retain this license notice if you want to use this software

ab -c100 -n10000 http://localhost:8888/ | grep "Requests per second" | awk '{split($0,a," "); split(a[4],b,"."); print b[1]}' > test/100x10000.dat
ab -c100 -n10000 http://localhost:8888/ | grep "Requests per second" | awk '{split($0,a," "); split(a[4],b,"."); print b[1]}' >> test/100x10000.dat
ab -c100 -n10000 http://localhost:8888/ | grep "Requests per second" | awk '{split($0,a," "); split(a[4],b,"."); print b[1]}' >> test/100x10000.dat
ab -c100 -n10000 http://localhost:8888/ | grep "Requests per second" | awk '{split($0,a," "); split(a[4],b,"."); print b[1]}' >> test/100x10000.dat
ab -c100 -n10000 http://localhost:8888/ | grep "Requests per second" | awk '{split($0,a," "); split(a[4],b,"."); print b[1]}' >> test/100x10000.dat

cat test/*.dat | sort






