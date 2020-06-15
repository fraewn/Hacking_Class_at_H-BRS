64 bit 8 bytes
p16 schreibt 2 byte
und nur zwei byte da rein
aber nur letzten bieden bytes der adressen
und erstmal ruas finden wie viele buchstaben da rein finden der muss voll sein


## Vorbereitungen 
1. file overwret me
2. checksec overwret me 
stack canary no --> buffer overflow möglich
relro no --> können global offset table manip. 
no pie --> 
3. strings overwretme
nur um mal zu gucken was es so gibt
4. objdump --syms overwretme oder objdump -j .text --syms overwretme
seiht man nochmal funktoinen unso 
5. readelf 

* es war nichts von libc da drin damit es einfacher war da durch zu steigen und den flow zu erkennen
* fängt wirklich bei start an und dann main 
##  Ablauf
* 30h in stack 
* dann esi und edi machen iwie die system calls erstmal write und dann stdout 
* wir hatten keinen pi deshalb konnten wir ausnutzen das adresse immer gleich war
* buffer overflowen und return adresse überschreiben 
* dann wird die adresse von uns da rein getan und im flow des programms aufgerufen
* dann musste man das interactive dings anmachen in pwn tools damit man mit der shell komm. konnte
* nx war zwar enabled aber wir konnten trotzdem code ausführen, weil sich das nx nur auf die bereiche bezieht, die nicht ausführbar sein sollen
* und wir haben einfach code genutzt der ausführbar hätte sein sollen weil er in der text section war: also wir mussten code nehmen der schon da war
