  
from Crypto.Cipher import AES
from Crypto import Random
import time
start_time = time.time()

import os
#generate 16 byte key
start_time = time.time()
key=os.urandom(16)
print("key generation time :- %s seconds " % (time.time() - start_time))
    
#blocksize of AES as required
blocksize=AES.block_size
    
def encryptm(input_file,key):
        f=open(input_file,"rb")
        plaintext=f.read()
        
        filesize=len(plaintext)
        padding_reqd=(blocksize -filesize) % blocksize
        plaintext=plaintext + b"\0" * padding_reqd
        in_vector = Random.new().read(blocksize)
        cipher=AES.new(key, AES.MODE_CBC, in_vector)
        start_time = time.time()
        encrypted=in_vector + cipher.encrypt(plaintext)
        print("encrypt mb time :-%s seconds " % (time.time() - start_time))
        f=open("encryptedmb.txt","wb")
        f.write(encrypted)
        
def decryptm(input_file,key):
        f=open("encryptedmb.txt","rb")
        ciphertext=f.read()
        in_vector=ciphertext[:blocksize]
        cipher = AES.new(key, AES.MODE_CBC, in_vector) 
        start_time = time.time()
        decrypted=cipher.decrypt(ciphertext[blocksize:])
        print("decrypt mb time :-%s seconds " % (time.time() - start_time))
        dec=decrypted.rstrip(b"\0")
        f=open("decryptmb.txt","wb")
        f.write(dec)
    
encryptm("mb file.txt",key)
decryptm("encryptedmb.txt",key) 
    

#for small size
def encrypt(input_file,key):
        f=open(input_file,"rb")
        plaintext=f.read()
        
        filesize=len(plaintext)
        padding_reqd=(blocksize -filesize) % blocksize
        plaintext=plaintext + b"\0" * padding_reqd
        in_vector = Random.new().read(blocksize)
        cipher=AES.new(key, AES.MODE_CBC, in_vector)
        start_time = time.time()
        encrypted=in_vector + cipher.encrypt(plaintext)
        print("encrypt kb time :-%s seconds " % (time.time() - start_time))
        f=open("encryptedkb.txt","wb")
        f.write(encrypted)
        
def decrypt(input_file,key):
        f=open("encryptedkb.txt","rb")
        ciphertext=f.read()
        in_vector=ciphertext[:blocksize]
        cipher = AES.new(key, AES.MODE_CBC, in_vector)
        start_time = time.time()
        decrypted=cipher.decrypt(ciphertext[blocksize:])
        print("decrypt kb time :- %s seconds " % (time.time() - start_time))
        dec=decrypted.rstrip(b"\0")
        f=open("decryptkb.txt","wb")
        f.write(dec)

encrypt("kb file.txt",key)
decrypt("encryptedkb.txt",key)
    

    

#https://www.guru99.com/reading-and-writing-files-in-python.html
#https://www.dlitz.net/software/pycrypto/api/current/Crypto.Cipher.AES-module.html
    
        