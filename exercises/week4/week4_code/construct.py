#!/usr/bin/env python3
# PyCrypto(!) not PyCryptoDome
from Crypto.PublicKey import RSA

# also das hier ist schon passiert
# die flag wird aus flag.txt ausgelesen
flag = open("flag.txt", "rb").read()
# dann wird eine neue RSA Verschlüsselung generiert, die
# die länge des modulos wird auf 2048 festgelegt
# der exponent ist 7
# es folgt dass der rsa ciphertext und die rsa signature genau so lang sind wie das modulo
# bei 2048 bit modulo sind das 256 bytes
r = RSA.generate(2048, e=7)
# c ist dann der ciphertext (die flag, die mit RSA verschlüsselt wurde)
# paramter: das was encrypted werden soll (plaintext)
# paramter2: und dann ein random parameter (byte string or long) - A random parameter (for compatibility only. This value will be ignored)
# r.encrypt returns A tuple with two items. The first item is the ciphertext of the same type as the plaintext (string or long). The second item is always None.
# also ist in c der ciphertext der flag gespeichert
c = r.encrypt(flag, "")[0]

ofile = open("output.txt", "w")
# der ciphertext in hex
print(c.hex(), file=ofile)
# the modulus
# also hab ich den modulus gegeben
print(r.n, file=ofile)

