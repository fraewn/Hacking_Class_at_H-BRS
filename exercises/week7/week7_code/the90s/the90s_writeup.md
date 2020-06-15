## Vorbereitungen 
* checksec: nichts ist an, alles rot 
* d.h. wir können alle rücksprungadressen überschreiben
* wir könnten allen code der von der binary gemapped wurde 
* wir könnten die global offset table überschreiben 
* es wurde iwie an segmenten rumgepfuscht (sehen wir an has rwx segments)

## intro 
* es geht darum, dass die aufgabe fast genau so ist wie in overwret
* es wird bisschen mehr eingelesen 
* aber die datei wurde anders kompiliert (hier haben wir mehr möglichkeiten; siehe checksec)

## gucken wie viele zeichen man braucht zum überschneiden 
* cycling pattern 

##
* 