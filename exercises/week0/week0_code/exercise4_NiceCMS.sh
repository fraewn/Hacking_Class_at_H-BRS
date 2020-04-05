# look at website here: http://hack.hctf.fun:37366
# find the admin script here: https://hack.redrocket.club/downloads/16/
# make a get request to url without having "redirecting" enabled
# since curl automatically not redirects you it was sufficient
# flag was found somewhere in the body
curl "http://hack.hctf.fun:37366/admin.php" -v
