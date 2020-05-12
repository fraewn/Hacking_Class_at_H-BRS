## this is the given source code from the task

import secret
import ecdsa
import os

os.chdir("/opt")

key = open("secp256k1-key.pem").read()
# sk: signing key --> hier wird der private key genutzt
sk = ecdsa.SigningKey.from_pem(key)

pubkey = open("pub.pem").read()
# vk: verifying key  --> hier wird der public key genutzt
vk = ecdsa.VerifyingKey.from_pem(pubkey) 

# step 1.2
def sony_rand(n):
    # nonce
    return secret.LONG_CONSTANT

# step 1.2
def sign(data):
    # man darf nicht einfach admin eingeben
    if data == b"admin":
        raise ValueError("Not Permitted!")
    # ich glaub wird die nonce mehrfach verwendet
    # wenn man einen anderen username als admin nimmt,
    # wird der signing key mit der eliptischen Kurve benutzt:
    # man tut den username und die mehrfach verwendete nonce rein
    # und kriegt eine signature
    signature = sk.sign(data, entropy=sony_rand)
    return signature

# step 2.2
def check_signature(msg, sig):
    try:
        # hier wird die signatur und die message benutzt
        # um zu verifyen mit dem public key und der elliptischen kurve
        vk.verify(sig, msg)
        return True
    except ecdsa.BadSignatureError:
        return False

# step 1.1
def sign_user():
    # sign
    ## der username wird in variable data als hex gespeichert
    data = input("Your username:").encode()
    ## die signatur wird mit der methode sign(data) generiert und als hex gespeichert in der variable sig
    sig = sign(data).hex()
    ## der username wird decoded zurück gegeben und das token wird encoded zurück gegeben
    print("Your token:" + data.decode() + "," + sig)

# step 2.1
def verify_user():
    # verify
    data = input("Submit signed user token:")
    # variable user: username
    # variable signature: die signature
    user, signature = data.split(",")
    # die signature wird von hex in bytes umgewandelt
    sig = bytes.fromhex(signature)
    # dann wird geguckt, ob die signatur die vom admin ist oder nicht
    # parameter 1: die msg: der username in hex
    # paramter 2: signatur: die signatur in bytes
    if check_signature(user.encode(), sig):
        if user == "admin":
            print("Holy 1337, here have a flag:")
            print(secret.FLAG)
        else:
            print("Hello ", user)
            print("NO FLG 4 U")
    else:
        print("Invalid Signature Detected. This incident will be reported!")

sign_user()
verify_user()

