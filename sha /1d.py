#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time

import hashlib
filename ="kb file.txt"
f=open(filename,"rb")
bytes = f.read() 
start_time=time.time()
hashop = hashlib.sha256(bytes).hexdigest();
print("\ntime reqd for sha256 for kb file:- %s seconds" % (time.time()- start_time))
print("SHA 256 hash output for kb file :-\n\n",hashop)

import hashlib
filename ="mb file.txt"
f=open(filename,"rb")
bytes = f.read() 
start_time=time.time()
hashop = hashlib.sha256(bytes).hexdigest();
print("\ntime reqd for sha256 for mb file:- %s seconds" % (time.time()- start_time))
print("SHA 256 hash output for mb file :-\n\n",hashop)

import hashlib
filename ="kb file.txt"
f=open(filename,"rb")
bytes = f.read() 
start_time=time.time()
print(hashlib.sha512(bytes).hexdigest())
print("\ntime reqd for sha512 for kb file:- %s seconds" % (time.time()- start_time))
print("SHA 512 hash output for kb file :-\n\n",hashop)

import hashlib
filename ="mb file.txt"
f=open(filename,"rb")
bytes = f.read() 
start_time=time.time()
hashop = hashlib.sha512(bytes).hexdigest();
print("\ntime reqd for sha512 for mb file:- %s seconds" % (time.time()- start_time))
print("SHA 512 hash output for mb file :-\n\n",hashop)

#https://www.quickprogrammingtips.com/python/how-to-calculate-sha256-hash-of-a-file-in-python.html

#SHA3-256
#https://pycryptodome.readthedocs.io/en/latest/src/hash/sha3_256.html
from Crypto.Hash import SHA3_256
hashobj = SHA3_256.new()
filename ="kb file.txt"
f=open(filename,"rb")
bytes = f.read() 
hashobj.update(bytes)
start_time=time.time()
print (hashobj.hexdigest())
print("\ntime reqd for sha3-256 for kb file:- %s seconds" % (time.time()- start_time))


from Crypto.Hash import SHA3_256
hashobj = SHA3_256.new()
filename ="mb file.txt"
f=open(filename,"rb")
bytes = f.read() 
hashobj.update(bytes)
start_time=time.time()
print (hashobj.hexdigest())
print("\ntime reqd for sha3-256 for mb file:- %s seconds" % (time.time()- start_time))




