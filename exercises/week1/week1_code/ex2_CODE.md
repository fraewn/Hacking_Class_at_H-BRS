## CODE 

url: http://vuln2.redrocket.club:8000/index.php?

* an dem "inlude" konnte man sehen dass die app eine vulnerability bzlg. dynamic code loading hat
* hier gibt es 5 Möglichkeiten: 
* access.log konnte man nicht aufrufen
* link injection war verboten im code
* php stream rapper konnte man nur für die base64 encodete ausgabe von php-files nehmen, aber nicht für die ausgabe der flag.txt
* nachher stellte sich auch raus dass die flag-datei gar nicht flag.txt hieß (es war aber als tipp gegeben, dass man RCE haben musste)
* php stream rapper output von der file ging auch nicht (a) weil file wrapper verboten waren, b) weil die flag.txt ja auch anders hieß, aber das wusste ich halt nicht
* es blieb noch session file insertion (ich hatte keine ahnung wie powerful das ist)

Lösung
http://vuln2.redrocket.club:8000/index.php?name=<?php $_OUTPUT = shell_exec('cd ..; cd ..; cd ..; cd opt; cat flag_65223092309ijwjdas.txt'); echo $_OUTPUT; ?>&page=/tmp/sess_abc....

wobei abc... dann die session id ist (kann man im browser sehen)

Das funktioniert, weil wir indem wir die session kontrollieren, uns die Möglichkeit eröffnen in den name parameter php code zu schreiben. dann sind wir sozusagen "trusted" und es wird ausgeführt was wir wollen. Weil das was im name steht geprinted wird, also auch auf der konsole ausgeführt wird, funktioniert das (laut fabian). 

