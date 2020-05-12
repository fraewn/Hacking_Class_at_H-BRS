# das hier ist richards lösung

# 1. Die verwendete ellptische Kurve nennt scih secp256k1
# 2. In der Python Bib muss man dazu SECP256k1 importieren:
#	from ecdsa.curves import SECP256k1
# 3. k ist ein cryptographically secure random integer
#    er muss für jeden Signiervorgang neu gewählt werden
#    Allerdings ist der Wert für k hier fix, und wird auf eine unbekannte konstante gesetzt:
#          import secret
#          secret.LONG_CONSTANT
# 4. Mehrere Signaturen liefern einen identischen ersten Teil, was eine Folge des konstanten k's ist:
#    test1,0589abade28762eea832854f89f6f144e4ef8ba27c03026f38eac070349b98a1 abab8fc6c02473c51f60e68708a570fd94c2bccc8cbaa3e1f1b84ea924436278
#    test2,0589abade28762eea832854f89f6f144e4ef8ba27c03026f38eac070349b98a1 7e7e874924a5c3ed5f71a8edb33047ce5cd16ccf92518574c98b7764386bac2a
#    test3,0589abade28762eea832854f89f6f144e4ef8ba27c03026f38eac070349b98a1 0a8381001666400d0f4927ae3cb1cb46385eba74d2eb83ff7a5a14580f667b7c
#    test4,0589abade28762eea832854f89f6f144e4ef8ba27c03026f38eac070349b98a1 7dc804524f3f62f7f8f1813c08cb8e564aa4cbe82c94bf0814c8e5c0eb16c8da
#    Die beiden Teile der Signatur repräsentieren das Zahlenpaar r,s aus dem Wikipedia Artikel, kann sein, dass das ein ranziger Punkt auf der noch ranzigeren Kurve ist
#    Es ist erkenntbar, dass r immer gleich ist
# 5. Dies bedeutet, dass im aktuellen Fall eine ähnliche Sicherheitslücke wie bei Sony vorliegt
#    die entropy, die zum signieren verwendet wird ist eine konstante
# 6. Im wikipedia-Artikel stehen die Formeln, die man verwenden muss um k und den secret Key dA zu erhalten
#    für den Fall, dass die entropy wie bei sony konstant ist
#    Damit kann das untenstehende Programm geschrieben werden um eine Fake Nachricht zu signieren


from hashlib import sha1
from ecdsa import SigningKey, SECP256k1
from gmpy2 import invert

hashfunc = sha1


r = int("0589abade28762eea832854f89f6f144e4ef8ba27c03026f38eac070349b98a1", 16)
print("r:  "+str(r))
s1 = int("abab8fc6c02473c51f60e68708a570fd94c2bccc8cbaa3e1f1b84ea924436278", 16)
print("s1: "+str(s1))
m1 = "test1".encode()
s2 = int("7e7e874924a5c3ed5f71a8edb33047ce5cd16ccf92518574c98b7764386bac2a", 16)
print("s2: "+str(s2))
m2 = "test2".encode()

z1 = int(hashfunc(m1).hexdigest(), 16)
z2 = int(hashfunc(m2).hexdigest(), 16)

n = SECP256k1.order # n Wert, Ordnung des Generators
print("n:  "+str(n))

k = (((z1 - z2) % n) * invert(s1 - s2, n)) % n
print("k:  "+str(k))

dA = ((((s1 * k) % n) - z1) * invert(r, n)) % n
print("dA: "+str(dA))

sk = SigningKey.from_secret_exponent(dA, curve=SECP256k1)
fakesig = sk.sign("test3".encode(),k=k)

print("orig: 0589abade28762eea832854f89f6f144e4ef8ba27c03026f38eac070349b98a10a8381001666400d0f4927ae3cb1cb46385eba74d2eb83ff7a5a14580f667b7c")
print("fake: "+str(fakesig.hex()))


sk = SigningKey.from_secret_exponent(dA, curve=SECP256k1)
fakesig = sk.sign("admin".encode(),k=k)
print("admin sig: "+str(fakesig.hex()))







