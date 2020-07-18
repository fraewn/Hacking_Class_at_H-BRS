from Crypto.Cipher import AES
from secret import key, flag, iv
import os

# hier wird was mit AES encrypted
# IV wird reingegeben
# es wird cipher block chain mode benutzt
aes = AES.new(key, AES.MODE_CBC, iv)
# es wird die IV in hex ausgegeben und direkt danach die encryptete flag auch in hex
print(iv.hex() + aes.encrypt(flag).hex())

# dann wird der key in hex ausgegeben aber die letzten 4 fehlen
print(key.hex()[:-4]) # Lets not make it that easy