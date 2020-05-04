from Crypto.PublicKey import RSA
from gmpy2 import iroot
import os



#Attacking textbook RSA with too short message
ciphertext_number = int.from_bytes(bytes.fromhex("6b8bb7bb5c1aff44a267e5eb06e846cef353db678b80d117b7aedc672afd453012df5de891bc15c6d8ac3fc3d9077c0aac7479c4741fd7bf5ffb20f04e18a318a5fc75e00fa1874797b5ae81dcc6223e3402f5"), "big")
print(ciphertext_number)
ciphertext_root = int(iroot(ciphertext_number, 7)[0])

recovered = ciphertext_root.to_bytes(16, "big")
print(recovered) #result: b'\x00\x00\x00\x00flag{kk_lol}'
