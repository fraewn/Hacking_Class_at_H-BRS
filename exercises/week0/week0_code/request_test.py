import requests

# see https://requests.readthedocs.io/en/master/user/quickstart/

# GET
# make a normal get request without anything and save status code and content type
r = requests.get('https://api.github.com/events')
statuscode = r.status_code
allheaders = r.headers
contenttype = r.headers['content-type']
text = r.text
# make text look nicer with json decoder
json_decoded_text = r.json()
encoding = r.encoding

# make url request at google with params: language is german and search word is 'miley'
searchparams = {'hl': 'de', 'q':'miley'}
search_with_params = requests.get('https://www.google.com/search?', params=searchparams)

# make url request with specified header that we send to server
headers = {'user-agent': 'firefox'}
request_with_header = requests.get('https://www.github.com', headers=headers)

# access cookies



# get test functions
print('GET REQUEST TESTS')
print('test get request: ')
print(statuscode)
print(allheaders)
print(contenttype)
print(encoding)
print(text)
print(json_decoded_text)
print('\ntest get request with params: ')
print(search_with_params.status_code)
print('\ntest get request with headers in request: ')
print(request_with_header.status_code)

# POST
# simple web service where you can practice rest and make post requests and stuff
# important to not forget the /post part in the url
url = 'https://httpbin.org/post'

# create some basic content
content =  {'name': 'elena', 'beruf': 'Anglerin'}
# make post request to url, put content in data parameter
post_request = requests.post(url, data=content)

# create advance content with several values under the same key
#{
#  ...
#  "form": {
#   "key1": [
#     "value1",
#     "value2"
#    ]
#  },
#  ...
#}
advanced_content = [('name', 'elena'), ('name', 'sophia')]
advanced_post_request = requests.post(url, data=advanced_content)

# print
print('\n\nPOST REQUEST TESTS')
print('test simple post request with some content:')
print(post_request.status_code)
print(post_request.json())
print('\ntest advanced post request with proper content:')
print(advanced_post_request.status_code)
print(advanced_post_request.json())
