## Java LCG

## Intro 
* dieser python code ist zum testen gegeben 
* damit kann man erst mal hübsch code schreiben und den zu knacken 
* dann kann man das vllt auf die java impl. anwenden 
* bei der gegebenen app hab ich ja a,b,m gegeben 
* d.h. ich kann einfach selbst die nächste Zahl berechnen

## Java LCG
* das Seeed bestimmt halt den Anfang 
* es ist egal wie lang es ist
* aber falls jemand versucht das seed zu brutforcen wäre es wahrsch blöd, wenn es kurz ist 
* ich frag mich halt, ob es bei dem java programm auch so ist, dass das seed iwie noch geändert wird
* und ob das wichtig ist, um es zu hacken 
* 2^48-1 = 281474976710655
* 2^48 = 281474976710656


## Python bitwise operators 
* wenn eine bitwise operationen mit zwei Inputs (z.B. Integern) durchgeführt wird, 
werden diese zunächts in binary zahlen umgewandelt und dann wird für jedes bit die Operation durchgeführt
* in python gibt es mehrere solcher Operationen: https://wiki.python.org/moin/BitwiseOperators
* shift bits: x << y returns x with its bits shifted by y places to the left 
Beispiel: 
```python
bit = 1029 
# bits: 10000000101
print("{0:b}".format(bit))
# bit << y
# shifted to the left: 1000000010100 (just two zeros are added)
print("{0:b}".format(bit << 2))
# same result as if we multiplied bit with 2^2 (second two is the multiplier y)
print("{0:b}".format(bit * 2**2))
# bit >> y
# shifted to the right: 100000001
print("{0:b}".format(bit >> 2))
`````
* & operator: does logical and to each bit
example
```python
bit = 1029 
# 1029 (they are the same)
print(bit & bit)
# 1028 
print(bit & (bit+1))
# because: 
# bit:   10000000101
# bit+1: 10000000110
# bit & bit+1: 10000000100
```
* bitwise exclusive or: x ^ y 
example: 
```python
bit = 1029 
# 0 
# xoring the same strings is 0 cause if two bits are the same, the result is 0 
print("{0:b}".format(bit ^ bit))
```

## SOLUTION
* tatsächlich konnte man anscheinend annehmen, dass die Implementierung in Java fast die gleiche war wie die in python 
* dh. die ganzen Parameter waren gleich
* das einzige was anders war, war dass man nicht den kompletten output hatte
* sondern nur einen Teil 
* dann können wir wie in den Videos beschrieben den Rest der fehlenden bits brute forcen 
* und dann damit den nächsten output generieren 
* die Lösung ist in ex2_javalcg_exploit.py 









