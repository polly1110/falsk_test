# send request
import requests

BASE = "http://127.0.0.1:5000"
response = requests.get(BASE + "/helloworld")
data = response.json
response_post = requests.post(BASE + "/helloworld")
#print(data)
print(response_post.content)