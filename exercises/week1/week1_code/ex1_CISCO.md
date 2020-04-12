## CISCO

url: http://vuln2.redrocket.club:8009

Es geht um einen ping service, d.h. wir können da ne adresse eingeben und dann führt der service ein ping durch und verschickt 2 testpakete (ping -c 2 www.google.de). die webadresse die gepingt werden soll, kann über den target parameter eingegeben werden. Der ping wird ja auf der shell ausgeführt, daher müssen wir es iwie schaffen hinter die webadresse noch das was wir eig. ausführen wollen zu packen. Es war verboten leerzeichen zu machen sowie semikolons und noch iwas. Das leerzeichen kann man mit ${IFS} ersetzen. Das ; kann man ersetzen indem man einfach einen nicht ausfühbaren befehl macht und dann || weil dann wird automatisch noch der nach dem oder ausgeführt. 

Bei der Aufgabe war fies dass die flag nicht direkt angezeigt wurde. Man musste sich den code mit strg + u bzw. inspect angucken und dann wurde die dort erst angezeigt. 

Lösung: 
http://vuln2.redrocket.club:8009/?target=123.t0||cat${IFS}flag.txt

