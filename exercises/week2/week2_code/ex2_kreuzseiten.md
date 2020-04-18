# KREUZSEITEN

## Intro 
url: http://vuln3.redrocket.club:8111/
* quotes kann man über get anzeigen mit dem Paramter msg: /?msg=Mamas+sind+die+Besten
* allerdings wird nirgendwo was gespeichert, weil man kann sich auch random quotes anzeigen lassen, die noch keiner hinzugefügt haben kann
* man kann bugs reporten indem man die url dazu einfügt (das hört sich nach einer Schwachstelle an)
* da die Aufgabe Kreuzseiten heißt, geht man von cross site scripting aus (xss)
* Fabian meint man braucht einen webserver und muss sich das access log anzeigen lassen 
(macht ja auch sinn weil wir greifen den enduser an)

ich muss den apache server wieder stoppen: https://www.tecmint.com/install-apache-web-server-in-a-docker-container/




