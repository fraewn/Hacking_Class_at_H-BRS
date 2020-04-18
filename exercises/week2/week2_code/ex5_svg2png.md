# SVG2PNG

* man muss eine xxe (xml external entity) attack machen via svg2rlg call 

## Intro 

1. Code studieren: svg2png.py

2. Schwachstelle finden für xxe Attacke 
* vllt muss man statt einer svg-File eine xml-File hochladen 
* die Flag ist hier: /opt/key.txt und ist auch in app.secret_key gespeichert --> svg2png.py 

Hinweise waren hier: 
* https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-10799
* https://github.com/deeplook/svglib/issues/229

## Vorgehen
Aus den Hinweisen geht hervor, dass in dem svglib-Package von Python eine Schwachstelle ist: 
Man kann auf Dateien des System zugreifen, indem man in die svg-Datei eine xml external entity rein packt. 
Diese muss das SYSTEM-Keyword haben und einen Link zu der File. Die Flag liegt laut python-code in "/opt/secrect_key". 

Die erstellte .svg-file liegt in xee.svg. Sie beinhaltet die XXE und zeigt auf den Pfad zur Flag. Außerdem mussten
Schriftgröße, Fenstergröße usw angepasst werden. 

Wichtig war auch beim Prozess des Ausprobierens, die in private Funktion des Browsers zu nutzen, da sich sonst
die Ergebnisse wiederholten (d.h. auch bei der selben File kamen immer wieder die gleichen schlechten vorangegangen Ergebnisse. Anscheinend
wurden die zuvor hochgeladenen files irgendwie im Browser gespeichert und statt der neuen aktuellen file hochgeladen). Auch beim in private
Browsen mussten man das Fenster dann ab und zu schließen (nach ca. 5 mal) und neu beginnen, damit überhaupt die neue file
genommen wurde. Sehr strange, aber gut zu wissen. Linux Firefox Browser 

Der Inhalt der file wurde dann als png angezeigt und konnte abgelesen werden: 
flag{https://www.youtube.com/watch?v=e5nyQmaq4k4#N1c3_W0rk!}
 