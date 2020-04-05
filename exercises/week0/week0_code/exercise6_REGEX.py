import requests

# quick script to check if the content contains a flag for many userids
# this did not solve the hack!

url = "http://vuln.redrocket.club:4444/?"
flag = "no flag found"

for i in range(1,1000):
    # create userid
    if(i<10):
        uid = str(0) + str(0) + str(i)
    elif(i<100):
        uid = str(0) + str(i)
    else:
        uid = str(i)

    # creater parameters for get request and insert userid
    params = {'uid': uid}
    # make get request with userid as parameter
    r = requests.get(url, params=params)

    # print progress
    # print("\nRequest_no: " + str(i))
    # save page content
    content = str(r.content)
    # print content
    #print(content)

    # check if there is a string "Flag" in the content
    if "Flag" in content:
        # save userid that leads to flag
        flag = "here:" + str(i)

print(flag)



