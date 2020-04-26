from Crypto.Cipher import AES
from secret import key, flag, iv
import os

# es wird ein neuer key in ciphertext block chaining mode erstellt
# es wird ein init. vector benutzt
aes = AES.new(key, AES.MODE_CBC, iv)
# ausgegeben wird der initialisation vektor in hex und die damit encryptete flag in hex
print(iv.hex() + aes.encrypt(flag).hex())

# und dann wird noch der key ausgegeben, wobei die letzten vier zeichen fehlen
print(key.hex()[:-4]) # Lets not make it that easy
