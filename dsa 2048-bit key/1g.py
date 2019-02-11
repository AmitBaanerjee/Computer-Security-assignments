from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dsa
import time
start=time.time()
private_key = dsa.generate_private_key(key_size=2048,backend=default_backend())
print(time.time()-start)

f=open("kb file.txt","rb")
data=f.read()

start=time.time()
signature = private_key.sign(data,hashes.SHA256())
print(time.time()-start)

public_key = private_key.public_key()
start=time.time()
public_key.verify(signature,data,hashes.SHA256())
print(time.time()-start)

#MB file

f=open("mb file.txt","rb")
datamb=f.read()

start=time.time()
signature = private_key.sign(datamb,hashes.SHA256())
print(time.time()-start)


public_key = private_key.public_key()

start=time.time()
public_key.verify(signature,datamb,hashes.SHA256())
print(time.time()-start)

#https://pycryptodome.readthedocs.io/en/latest/src/public_key/dsa.html