import requests
import re



username = 'natas6'
password = 'fOIvE0MDtPTgRhqmmvvAOt2EfXR6uQgR'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()
response = session.post(url,data={"secret":"FOEIUWGHFEEUHOFUOIU","submit":"submit"},auth=(username,password),)

response = response.text
print(response)