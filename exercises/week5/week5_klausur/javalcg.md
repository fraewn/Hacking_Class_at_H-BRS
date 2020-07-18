## javalcg 

* in der app kommt das gleiche raus wie in das mit der python klasse berechnete in der next() Methode
* das, was ausgegeben wird, die random numbers sind die versch. states nachdem sie postprocessed wurden
* das heißt die echten states kenn ich nicht 
* Ziel: es schaffen, eine der echten states raus zu finden, um dann die Folge nummer zu berechnen, bevor sie ausgegeben wird 
* Strategie: 
    * das postprocessing reversen (jetzt hat man die echte state)
    * weil bei dieser Operation die 17 bits iwie verloren gegangen sind,
    * müssen wir die brute forcen. Mit + i hängen wir sie einfach an die echte state dran 
    * mit 17 bits (100000000000000000 bin = 131072 dec = 2**17) kann man so viele Zahlen ausrechnen, d.h. wenn es sein muss, rechnen wir bis zu +131072 auf unsere echte state drauf 
    * mit dieser die Folgestate berechnen 
    * postprocessing durchführen 
    * gucken ob das der richtigen Folge-Nummer entspricht 
    * dann mit der Folgestate die nächste State berechnen
    * wieder das postprocessing durchführen 
    * und das ist dann die nächste Nummer --> eingeben und flag abholen 
