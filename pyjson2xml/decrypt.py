#! /usr/local/bin/python

from cryptography.fernet import Fernet
import sys

def decrypt(file_to_decrypt, key):
    f = Fernet(key)

    with open(file_to_decrypt, 'rb') as encrypted_file:
        encrypted = encrypted_file.read()


    decrypted = f.decrypt(encrypted)
    filename = file_to_decrypt.split('/')[-1]
    with open(filename, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)

if __name__ == '__main__':
    file_to_decrypt = sys.argv[1]
    with open('/shared/crypto_key.key', 'rb') as mykey:
       key = mykey.read()
    
    decrypt(file_to_decrypt, key)

