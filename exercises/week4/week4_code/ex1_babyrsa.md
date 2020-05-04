# Ex1 BabyRSA

## Intro 
* modulus ist gegeben 
* cipher text in hex ist gegeben 
* evtl. muss man nach einer Schwachstelle suchen (warhsch von pycrypto)
* laut internet sind die keys weak 
* does not have semantic security?
* diffie hellman assumption does not hold for this package
* ich glaube es wurde kein padding verwendet
* evtl. könnte man ausprobieren, für jede anzahl mögl. längen der flag 

```
6b8bb7bb5c1aff44a267e5eb06e846cef353db678b80d117b7aedc672afd453012df5de891bc15c6d8ac3fc3d9077c0aac7479c4741fd7bf5ffb20f04e18a318a5fc75e00fa1874797b5ae81dcc6223e3402f5
```

Der Flag-Ciphertext hat 166 Zeichen (nicht 256, wie es sein sollte).

## Strategie 
* ciphertext in ints umwandeln 
* dann die formel nehmen um zu decrypten 

c = m^7 (2048)
166*7 < 2048
m = siebte wurzel aus c 