from Crypto.Cipher import AES
import os
from oauthlib.common import generate_nonce
from secret import key

NONCE = generate_nonce()

def encrypt(msg):
    # funktionsweise AES:
    # nonce + counter werden verschlüsselt mit einem key
    # dann wird der plaintext damit gexored
    # und das ist dan der ciphertext
    # AES sollte 16 byte blöcke haben
    aes = AES.new(key, AES.MODE_CTR, nonce=NONCE)
    # das ganze wird dann noch gehext
    # d.h. ein buchstabe entspricht zwei zeichen
    return aes.encrypt(msg).hex()
#5cd9430d66c0245e6691568fef403d79
#8711d6da2d63298678978711e5ec78a5
#c2

# die beiden gleichen zeichen gegen die dinger schießen und dann müsste ja da wo die zeichen gleich sind das zeichen der nonce sein
# if we flip bits in the cipher text, bits in the plain texts are flipped



print(encrypt("hello"))
q = input("Encrypt this string:").encode()
# dann wird erst q also "Encript this string:" geprintet
print(q)
# und danach wird das encryptete von encrypt this string geprinted
print(encrypt(q))