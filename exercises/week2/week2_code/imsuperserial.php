<?php
include("db_driver.php");

// Defintion der Klasse ShellCommand
class ShellCommand {
   // Prüfung ob Wert der variable $cmd "ok" ist
   function is_ok($cmd) {
           return false;  // disabled for now
   }
   // hier wird die Prüfung aufgerufen
   function __construct($cmd) {
      if ($this->is_ok($cmd)) {
         // hier wird in dem ShellCommand-Objekt das Attribut cmd auf den Wert der Varialbe $cmd gesetzt
         $this->cmd = $cmd;
      }
   }
   function exec() {
       system($this->cmd);
   }
}

// Defintion der Klasse DB
class DB {
    // dem Attribut db_driver dieser Klasse wird ein neuer DBDriver zugewiesen
    function __construct() {
        $this->db_driver = new DBDriver();
    }
    // führt eine query auf der db auf, unter Benutzung des db_driver Attributes (was ja ein DBDriver ist)
    function exec($query) {
        // sie gibt das Ergebnis von do_query zurück
        return $this->db_driver->do_query($query);
    }
}

// Defintion der Klasse User
class User {
    // Konstruktor; weißt allen attributen der Klasse User Werte von Variablen zu
    // es gibt eine userid, einen namen eine db und ein active ja oder nein
    function __construct($uid, $name) {
            $this->uid = $uid;
            $this->name = $name;
            // Attribut db bekommt neue Datenbank
            // die DB ist die DB Klasse
            $this->db = new DB();
            $this->active = true;
    }
    // über Attribut db können queries direkt ausgeführt werden
    function __wakeup() {
        // hier werden ALLE tables aus Tabelle Sessions von einem user geholt (der mit dieser userid)
        // wenn was da was zurück kommt, ist die Session noch aktiv
        if ($this->db->exec("SELECT * FROM SESSIONS WHERE uid=". $this->uid)) { // session still active
            // dann wird das Attribut active der Klasse User auf true gesetzt
            $this->active = true;
        } else {
            // dann wird das Attribut active der Klasse User auf false gesetzt
            $this->active = false;
        }
    }
}

// generell: falls ein cookie gesetzt ist mit value 'session'
// dann wird der Variable user der unserialized cookie zugewiesen (kein encoding)
if (isset($_COOKIE['session'])) {
    // hier wird ein user objekt erstellt
    $user = unserialize($_COOKIE['session']);
    // und dann kriegt man ne rückmeldung (die wird geprinted)
    echo "You are logged in as " . $user->name;
} else {
    // wenn kein cookie gesetzt wird, ist man ein guest user mit uid 1234 und name "guest"
    $cookie = new User(1234, "guest");
    // dann wird der cookie aus diesen Daten gesetzt
    setcookie('session', serialize($cookie));
    header("Location: /");
}