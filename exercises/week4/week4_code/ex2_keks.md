## Ex. 2 - keks 

## Intro 
* we were supposed to read about Bleichenbachers Attack 

## Bellcore Attack 
* es dauert lange, die msg hoch d modulo m zu nehmen 
* stattdessen kann man das aufteilen, indem man sich zur Nutze macht, dass m = p * q ist 
* p und q sind die beiden primzahlen, die halb so lang sind wie m 
* man rechnet dann msg^d mod p und msg^d mod q 
* aus diesen beiden Ergebnissen kann man mit dem chinesischen Restsatz msg^d mod m berechnen 
* wir erstellen eine Signatur auf diese Weise und bei einem der beiden Ergebnisse geschieht ein Fehler (z.B. bei q)
* darauß folgt Signatur^e = msg (mod p) aber Signatur^e != msg (mod q)
* wir können testen, ob die Signatur stimmt mit Signatur^e != msg (mod N)
* auch als Angreifer können wir das testen, wenn wir die volle message kennen 
* wir können die verschlüsselung dann knacken, indem wir den greates common divisor berechnen: gcd(N, Signatur^e - msg)
* dann kriegen wir nämlich q raus (wenn da der Fehler passiert ist)
* und weil d = inverse(e) (mod phi(N))
* phi(N) = phi(p*q) und p = N/q (im Moment kann phi(n) noch nicht so berechnet werden, weil n zu groß ist --> wir brauchen zwingend p oder q)
* und kriegen damit den Schlüssel d 

## test if an error did actually happen
* Signatur^e != msg (mod N)

## keks 
* wir haben den kompletten plaintext gegeben 
* wir wissen, wie die Signatur generiert wird (mit crt)
* d.h. entweder in allen, oder in ein paar von den Fällen, wird eine falsche Signatur generiert
* wir können das testen weil wir N und e gegeben haben 
* wenn der test sagt, dass die Signatur falsch ist, können wir d berechnen 
* und 
* 

## keks main.py 
* da kommt eine signatur rein
* das programm testet ob die signatur stimmt indem es sie hoch e und mod(m) nimmt
* 