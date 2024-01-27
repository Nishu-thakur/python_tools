import requests
import re

username = "natas26"
password = "8A506rfIAXbKKk68yJeuTuRq4UfcK70k"

url = "http://natas26.natas.labs.overthewire.org/"

session = requests.Session()
response = session.get(url+"",auth=(username,password))

content = response.text

print(content)