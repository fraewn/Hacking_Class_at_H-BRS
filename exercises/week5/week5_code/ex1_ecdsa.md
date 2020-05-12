## ECDSA

## Sources 
* https://en.wikipedia.org/wiki/Elliptic_Curve_Digital_Signature_Algorithm#Signature_generation_algorithm
* https://www.youtube.com/watch?v=-UcCMjQab4w
* eccfun/basics/examples/curves/ECDSA.py 
* https://github.com/mclab-hbrs/eccfun

## Intro 
#### Step 1
* man gibt einen username an
* und kriegt einen token 

#### Step 2
* man soll username, token angeben 
* das token soll "signed" sein und zwar als admin 

## Idee 
* man kann eine Signatur erstellen, die den user zum admin macht

## Umsetzung 
* man hatte halt diesen token und seinen username gegeben
* der Witz war, zu sehen, dass wenn man mehrere Token generiert, diese alle den gleichen Anfang haben: 
```shell script
# request 1
Your username:hello
Your token:hello,0589abade28762eea832854f89f6f144e4ef8ba27c03026f38eac070349b98a1a446205fee82f0c8996e28b6b02a7bcd34b9d253e48c54c5ba8d273b204a93e8
# request 2
Your username:h
Your token:h,0589abade28762eea832854f89f6f144e4ef8ba27c03026f38eac070349b98a1b836b092e190ea25355cddcf4d565398fdf33b5ba23426ee47ca46105b5b0f16
```
* dieser Teil der immer gleich ist, ist r 
* der andere Teil ist s
* und der username ist die message m 

## Vulnerability
* anscheinend wurde also immer dasselbe r benutzt und das kann man ausnutzen um k (die zahl die zum generieren der signatur benutzt wird, also die nonce) zu rekonstruieren
* das geht so wie in dem youtube video oben gezeigt und in wikipedia beschrieben 
