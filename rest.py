import requests
import json

url = 'https://en.wikipedia.org/w/api.php?action=query&titles=Pointer&format=json&formatversion=2'

r = requests.get(url)
print(r.status_code)

json_ob = json.loads(r.text)
print(json_ob)
