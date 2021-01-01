#! /usr/local/bin/python

from cryptography.fernet import Fernet
import sys

def encrypt(file_to_encrypt, key):
    f = Fernet(key)

    with open(file_to_encrypt + '.xml', 'rb') as myfile:
        original = myfile.read()

    encrypted = f.encrypt(original)

    with open('/shared/' + file_to_encrypt + '.xml', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

if __name__ == '__main__':
    file_to_encrypt = sys.argv[1].split('.')
    if file_to_encrypt[1] != 'xml':
        raise TypeError('Wrong file type! Expecting an xml file to encrypt')
    
    with open('/shared/crypto_key.key', 'rb') as mykey:
        key = mykey.read()


    filename = file_to_encrypt[0]
    encrypt(filename, key)

