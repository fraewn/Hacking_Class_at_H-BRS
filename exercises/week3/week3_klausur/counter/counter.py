from Crypto.Cipher import AES
from secret import key, flag, generate_nonce
import os

# hier wird so fake nonce generated
NONCE = generate_nonce()


def encrypt(msg):
    # neue symm. verschl.; counter mode wird verwendet; nonce wird von oben genommen
    # d.h. wenn das hier öfter aufgerufen wird; immer die gleiche nonce
    aes = AES.new(key, AES.MODE_CTR, nonce=NONCE)
    # die encryptete message wird als hex zurück gegeben
    return aes.encrypt(msg).hex()


# die flag wird mit der function encrypted
print(encrypt(flag))
# der service nimmt das hier entgegen
# und formatiert das von string zu bytes
q = input("Encrypt this string:").encode()
# dann nutzt der die encrypt funciton und encryptet das 
print(encrypt(q))