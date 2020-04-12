# SQLI2

## General Information

url: http://vuln2.redrocket.club:22345/

Das hier ist der zugehörige code in python: 
```python 
article_id = request.form["article_id"] 
title = request.form["title"] 

if "'" in article_id or "'" in title: return "Forbidden character used!" 

cursor.execute(f"SELECT id, title, content FROM articles WHERE public=1 AND (id='' OR title='')")
```

* eins von beiden kann immer leer bleiben
* nur die id wird wirklich gebraucht 
* man darf kein ' benutzen 
* " funktionieren 

## Wie muss die Query modifiziert werden? 
Die Query soll später so aussehen, dass union select durchgeführt werden kann: 

```sql
SELECT id, title, content FROM articles WHERE public=1 AND (id='  \'   \' OR title=' ) union select schema_name, 2, 3 from information_schema.schemata LIMIT 0,1 --') 
```

* also ich muss in das erste feld ein ' rein tuen 
- evtl. muss ich \ (quotation mark) \ einfügen damit das ganze als ein string erkannt wird (ja muss man definitiv, weil sonst wird das dritte semikolon als "string zu ende" gesehen und das will man ja nicht)
- und ich das zweite input feld muss ich kein ' rein tun weil da steht ja schon eins dann (was den string dann beendet)
- da muss ich nur das letzte ' vom zweiten input feld kaputt machen, indem ich da ein -- am ende hin tue 
- und da kommt dann also nur noch eine klammer zu hin (damit kein sql fehler kommt) 
- und dann meinen code rein 

Also was wird getan? 
erstes input Feld: 
Eingabe: \ ' \
id=' \' \' -- jetzt denkt die db der string geht noch weiter (weil das ende-des-string-anführungszeichen ist ja escaped). 
--> Funktioniert auch, wenn man nur \ rein tut 

zweites input feld: 
title=' -- hier ist der String jetzt zu Ende, dank dem anfang-des-string-anführungszeichen des zweiten inputs 
--> jetzt kann man seinen eigenen code rein tun (muss aber noch die klammer schließen damit es klappt)

### Wie umgeht man die Anführungszeichen-Sperre? 
Diese ist durch Python-Code umgesetzt. Die mysql-Datenbank übersetzt hex, ansi, url encodede strings in die richtige Bedeutung. Daher funktioniert folgendes um das Anführungszeichen zu ersetzen (alle ausprobiert):
* \ 0x27 \    -- hex encode 
* \ 0027 \   --ansi? encode 
* \ %27 \   --url encode 

Wie gesagt, hätte man das Anführungszeichen aber gar nicht gebraucht, sondern nur das \ Zeichen. 

### Welchen Code braucht man, um die flag anzuzeigen?
Da es sich um dieselbe DB wie bei Aufgabe 3 handelt, wurde der selbe String um die flag zu bekommen genommen: 
```SQL
) union select id, name, password from userdatathatisvaluable limit 0,1  --
```
Nur in diesem Fall wurde davor die Klammer gesetzt, damit kein SQL Fehler ausgegeben wurde. **Wichtig**: Im Eingabefeld musste nach den Kommentarstrichen noch ein Leerzeichen hinzugefügt werden, sonst wurde ein Fehler geworfen 







