import requests
import re

username = 'natas8'
password = 'a6bZCNYwdKqN5cGP11ZdtPg0iImQQhAB'
url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()
response = session.post(url,data={"secret":"oubWYf2kBq","submit":"submit"},auth=(username,password))

content = response.text

print(content)