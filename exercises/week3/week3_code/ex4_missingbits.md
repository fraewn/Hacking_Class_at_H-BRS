# Missing Bits 

## Output 
05ef9caa70722673e46d8fddc560ad04d225c8eb82b9bafe0a13e7f9f2e12f493f82c74d5ffdffb81e6021e3da818ec3
797a05c26d83f0579780252f147a

## Intro 
* Cipher Block chain mode ist used
* Attacke: byte flip ist hier möglich 
* außerdem könnte man versuchen die missing bits zu finden im key 
* in cbc mode hat der IV immer 16 bytes, d.h. in hex ist er 32 Zeichen lang 
Quelle: https://pycryptodome.readthedocs.io/en/latest/src/cipher/classic.html#cbc-mode
* Daraus folgt wenn iv+flag in hex 96 Zeichen haben, dass die flag in hex 64 Zeichen hat, d.h. in plaintext 32 Zeichen 
* d.h. man hat den BA des IV 
* man hat die encryptete flag als BA
* die encryptete flag ist glaub ich genau 2 blöcke lang, weil 64 Zeichen in hex und 32 in plain, d.h. 2*16 also zwei Blöcke
* und wir haben den key bis auf die letzten 4 Zeichen 

## Ablauf encryption cbc mode von vorn 
1. ciphertext wird mit key verschlüsselt 
2. verschlüsselter ciphertext wird mit IV gexored


## Ablauf encryption cbc mode von hinten 
 1. plaintext flag wird mit dem IV geoxred 
* dann wird das ergebnis mit dem key encrypted 
* der ciphertext wird dann mit dem nächsten block gexored 
* und das wird dann wieder encrypted usw. 

## Strategie 
1. 