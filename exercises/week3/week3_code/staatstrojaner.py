#AES, ECB: 
#Antworten des trojaners werden verschlüsselt
# über port 443 aber kein HTTPS sondenr eigens gebastelt
# dieses ist über AES ECB verschlüsselt

#1. encrypte screenshot wird gesendet message: 16 26 80 7c ff ff ff ff 00 26 80 7c 42 25 80 7c (aus dem CCC dokument) -> 9ec430650d29d678cc8e432a4ab720c7
#2. finde das paket in wireshark: Edit -> findpacketpaket -> hexvalue = 9ec430650d29d678cc8e432a4ab720c7. Ergebnis das Paket 4
#3. Rechtsklick follow tcp stream (tcp übertragugn wird in pakete aufgeteilt; wireshark baut dir aber den gnazen block zsm;
#4. format von ASCII auf RAW stellen 
#5. jetzt sieht man an beginn wieder den encrpyteten "screenshoots wird gesendet header" 9ec430650d29d678cc8e432a4ab720c7
#6. danach folgt das bild. Wo das bild anfängt erkennt man nach dem decrypten an der .jpg magic "ff d8" im hexstring relativ nah am anfang
#7. bild decrypted und als bytes in ein .jpg file schreiben

from Crypto.Cipher import AES
# encryption defininieren
key = bytes.fromhex("4903930819949694289383046828A8F50AB994024581931FBCD7F3AD93F53293")
aes = AES.new(key, AES.MODE_ECB)

# screenshot begins zu bytes umwandeln
a = bytes.fromhex('16 26 80 7c ff ff ff ff 00 26 80 7c 42 25 80 7c')
# encrypten, und wieder in hex darstellen
encrypted_screenshot_begins_header_hex = aes.encrypt(a).hex()
print(encrypted_screenshot_begins_header_hex) # 9ec430650d29d678cc8e432a4ab720c7 (gucken wo das paket mit dem hex string ist)


# find out where jpg starts
# take first 64 chars (because ECB needs fixed block size)
# convert hex to bytes
enc = bytes.fromhex('9ec430650d29d678cc8e432a4ab720c7af6200eb8a82709cb483a2485fe56d7f')
# decrypt
encrypted_begin_of_package_with_jpg = aes.decrypt(enc)
# you will see that jpg starts somewhere here because chars are in here
print(encrypted_begin_of_package_with_jpg)
# jpg actually starts later at 76th char for whatever reasons


 
aes = AES.new(key, AES.MODE_ECB)


decrypted = aes.decrypt(ciphertext)


f = open("flag.jpg", "wb")
f.write(decrypted)
