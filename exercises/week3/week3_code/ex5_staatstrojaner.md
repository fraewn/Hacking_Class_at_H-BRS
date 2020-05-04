## Staatstrojaner 

#### Intro
* es gab einen Staatstrojaner der iwie screenshots von client browsern gemacht hat 
* und dieses dann an eine feste server adresse verschickt
* man konnte die packages abfangen: traffic.pcap 
* die Encryption war AES in ECB mode, also relativ unsicher
* außerdem wurde der key rausgefunden 
* und man wusste das immer wenn der client ein bild an der server schickte das mit einem bestimmten String angekündigt wurde 
* Alle Infos sind hieraus: https://www.ccc.de/system/uploads/76/original/staatstrojaner-report23.pdf
* um .pcap Dateien also traffic-Mitschnitte auszulesen, eignet sich das tool wireshark 

#### Bekannt
key: `4903930819949694289383046828A8F50AB994024581931FBCD7F3AD93F53293` (bytes)
"screenshot begins header": `16 26 80 7c ff ff ff ff 00 26 80 7c 42 25 80 7c` (hex)

#### Strategie 
* flag ist wahrsch in so einem Bild 
* d.h. man muss
1. Packages dursuchen nach dem "screenshot begins header"
2. In dem Package das encryptete jpg finden und das entschlüsseln
3. encryptetes jpg in neue jpg file --> flag da drin 

#### Umsetzung 
1. Wireshark öffnen und .pcap-Datei darin öffnen 
2. Alles liegt in bytes vor: der Screenshot begins header liegt in plaintext in hex format vor 
Um den in den Paketen zu finden (da ist alles encrypted in hex), musste man ihn zunächst in einen bytearray umwandeln, dann mit 
AES in ECS mode und dem key encrypten und das dann nochmal wieder in hex umwandeln 
3. Dann in Wireshark mit dem Ergebnis suchen in welchem Paket es liegt (ging bei mir nicht gut, aber wusste es war Paket 4)
4. Dann das paket: rechtklick follow>tcp stream und Format von ascii auf raw stellen
--> Dann hatte man den ganzen inhalt des pakets (wo ja auch unser jpg drin ist) im raw format
5. jetzt musste man gucken, wo das bild tatsächlich beginnt
6. hierfür mal die ersten 64 bytes nehmen und decrypten 
7. dann findet man iwann diese zeichkombi aus 1626ff bla bla 
8. Später beginnt dann das Bild (ab dem 65. byte oder so)
9. das bild decrypten und in ein neues jpg schreiben 
