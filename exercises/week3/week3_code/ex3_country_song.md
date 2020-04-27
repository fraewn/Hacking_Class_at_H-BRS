## Country Song - ex. 3

#### Intro 
* es gibt eine doppel-verschlüsselung
* flag wird erst mit aes2 (key2) verschlüsselt, dann new line dran und das ganze in hex umgewandelt, dann in aes1 verschlüsselt (key1) und davor wird dann noch der IV in hex gepackt 
* die encryptete flag wird dann in einem png gespeichert
* vllt wenn das nach der 1. Verschlüsselung schon in hex vorliegt, ist das nach der zweiten dann autom. in hex? 
* bei png-Format wissen wir, dass das wieder ein bestimmtes Datei-Format sein muss und daher finden wir im Netz da einen 16 byte header zu in plaintext 
* außerdem haben wir das final encryptete gegeben 
* wir haben Teile der beiden keys, gegeben, die restlichen Teile müssen wir dann ausprobieren 

#### Strategie 
1. Wir kennen den png-Header, also die ersten 16 bytes des plaintexts
```
89504e470d0a1a0a
```

2. IV: 
Der IV steht ganz am Anfang der file und ist 16 bytes lang (weil AES). Da die file in hex vorliegt, ist er hier 32 Zeichen lang. 


3. key 1: 
Wir decrypten den gegebenen final encrypteten text mit allen möglichen Variationen von key1. Hierfür probieren wir alle möglichen byte-Kombination am Ende von key1 aus. 
Die Ergebnisse schreiben wir in eine Tabelle. 

4. key 2: 
Dann encrypten wir die gegebenen 16 bytes vom Plaintext mit allen möglichen Variationen von key 2. Hierfür probieren wir alle möglichen byte-Kombination am Ende von key1 aus. 
Die Ergebnisse schreiben wir in eine Tabelle. 

5. Vergleich 
Dann vergleichen wir die Inhalte in der Tabelle. 


