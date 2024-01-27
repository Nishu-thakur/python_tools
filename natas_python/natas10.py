import requests
import re


username = "natas11"
password = "1KFqoJXi6hRaPluAmk8ESDW4fSysRoIg"

cookies = {"data":"MGw7JCQ5OC04PT8jOSpqdmk3LT9pYmouLC0nICQ8anZpbS4qLSguKmkz="}

url = 'http://%s.natas.labs.overthewire.org/' %username

session = requests.Session()
response = session.get(url,auth=(username,password),cookies=cookies)



content = response.text

print(content)



