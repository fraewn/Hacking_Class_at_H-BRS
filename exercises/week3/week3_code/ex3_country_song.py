from Crypto.Cipher import AES
from Crypto.Util import Padding
from secret import key1, key2, iv
import os


flag = open("flag.png", "rb").read() #Flag is in this image

# flag wird gepadded weil die anscheinend sonst nicht lang genug ist
flag = Padding.pad(flag, 16) #Pad to 16 byte block length

# es gibt zwei keys
aes1 = AES.new(key1, AES.MODE_CBC, iv)
aes2 = AES.new(key2, AES.MODE_CBC, iv)


with open("output.txt", "w") as f:
    # der IV wird gehext und daran wird dann die mit key2 encrpytete und in hex umgewandelte flag nochmal mit aes1 also key 1 encrypted gehängt
    # also der output der doppel encrypten mit iv  vorne weg wird in die file geschrieben
    f.write(iv.hex() + aes1.encrypt(aes2.encrypt(flag)).hex() + "\n")
    # This time, three bytes are missing <@:-E
    # nicht rekursiv, sondern einmal die ersten keys durch rechnen
    # dann die zweiten durchrechnen und währenddessen vergleichen

    # in die file wir key1 in hex geschrieben (letzten 6 zeichen, also 3 bytes fehlen)
    f.write(key1.hex()[:-6] + "\n")
    # und key 2 auch
    f.write(key2.hex()[:-6] + "\n")