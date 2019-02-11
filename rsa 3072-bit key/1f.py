from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import time
start=time.time()
key = RSA.generate(3072)
print(time.time()-start)
private_key = key.export_key()
file_out = open("private.pem", "wb")
file_out.write(private_key)

pubkey = key.publickey().export_key()   
public= open("public.pem","wb")
public.write(key.publickey().export_key() )

encryptdata = b''
blocksize = 16

with open("kb file.txt","rb") as infile:
    block = infile.read(blocksize)
    while block: 
        publickey = RSA.importKey(open("public.pem").read())
        paddedpub = PKCS1_OAEP.new(publickey)
        encryptdata =encryptdata+ paddedpub.encrypt(block)
        block = infile.read(blocksize) 
    
infile.close()

with open("encryptedkb.txt",'wb') as outfile:
    outfile.write(encryptdata)

decryptdata = b''
blocksize = 384
with open("encryptedkb.txt","rb") as infile:
    block = infile.read(blocksize)
    while block:
        privatekey = RSA.importKey(open('private.pem').read())
        paddedpriv = PKCS1_OAEP.new(privatekey)
        decryptdata+=paddedpriv.decrypt(block)
        block = infile.read(blocksize) 

infile.close()
with open("decryptedkb.txt",'wb') as outfile:
    outfile.write(decryptdata)

encryptdata = b''
blocksize = 16


#------------------MB ----------------

encryptdata = b''
blocksize = 16

with open("mb file.txt","rb") as infile:
    block = infile.read(blocksize)
    while block: 
        publickey = RSA.importKey(open("public.pem").read())
        paddedpub = PKCS1_OAEP.new(publickey)
        encryptdata =encryptdata+ paddedpub.encrypt(block)
        block = infile.read(blocksize) 
    
infile.close()

with open("encryptedmb.txt",'wb') as outfile:
    outfile.write(encryptdata)

decryptdata = b''
blocksize = 384
with open("encryptedmb.txt","rb") as infile:
    block = infile.read(blocksize)
    while block:
        privatekey = RSA.importKey(open('private.pem').read())
        paddedpriv = PKCS1_OAEP.new(privatekey)
        decryptdata+=paddedpriv.decrypt(block)
        block = infile.read(blocksize) 

infile.close()
with open("decryptedmb.txt",'wb') as outfile:
    outfile.write(decryptdata)

