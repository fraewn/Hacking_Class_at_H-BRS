// java script code for exercise 3
// the generated pw was static so you just needed to make it visible via console.log and then enter it

// services we use, made accessable via variables
var http = require('http');
const crypto = require('crypto');
var url = require('url');
var fs = require('fs');

// strange variable. Is it an array?
var _0x777=["\xAF\xFE\x11","ff231231312312thisisnothex"];

// function that uses the crypto service to return a string
function generatePw() {
    return
         {
             //_0x777[1] = "ff231231312312thisisnothex"
             // crypto["ff231231312312thisisnothex"](8)
             x: crypto[_0x777[1]](8)
             console.log([x].toString(_0x777[0]))

         }[x].toString(_0x777[0]);
}

// method createServer gets a function as parameters
// method function gets two parameters request and result
http.createServer(function (req, res) {
    // we build the result by creating a header
    res.writeHead(200, {'Content-Type': 'text/html'});
    // we create a new variable passwd by attaching the result of generatePw() to the string "passwd"
    passwd = "passwd_" + generatePw();
    console.log(passwd)

    // we create a new variable url_content containing the content from the url?
    var url_content = url.parse(req.url, true);

    // we check if passwd is the same as the inserted passwd through the getrequest
    console.log(passwd)
    if (passwd == url_content.query.passwd) {
        console.log("hello")
       res.write(fs.readFileSync('flag.txt', 'utf8'));
    } else {
        var source = fs.readFileSync(__filename, 'utf8');
        res.write('<html><body><form method="get"><input type="text" name="passwd" value="password"><input type="submit" value="login" /></form></div></body></html>');
    }
    res.end();
}).listen(8888);