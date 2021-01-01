from cryptography.fernet import Fernet
import sys

# file_to_encrypt = sys.argv[1]

def generate_key():
    print('writing file')
    key = Fernet.generate_key()
    with open('/shared/crypto_key.key', 'wb') as crypto_key:
        crypto_key.write(key)

    return key

def read_key():
    with open('/shared/crypto_key.key', 'rb') as crypto_key:
        key = crypto_key.read()

    return key


def encrypt(file_to_encrypt, key):
    f = Fernet(key)

    with open(file_to_encrypt, 'rb') as myfile:
        original = myfile.read()

    encrypted = f.encrypt(original)

    with open('enc'+file_to_encrypt, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

# file_to_decrypt = sys.argv[1]

def decrypt(file_to_decrypt, key):
    f = Fernet(key)
    print(file_to_decrypt)
    with open(file_to_decrypt, 'rb') as encrypted_file:
        encrypted = encrypted_file.read()

    print(encrypted, 'encrypted')
    decrypted = f.decrypt(encrypted)
    with open("dec.xml", 'wb') as decrypted_file:
        decrypted_file.write(decrypted)


# decrypt(file_to_decrypt, key)

# encrypt(file_to_encrypt, key)

