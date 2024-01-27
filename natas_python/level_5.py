#!/usr/bin/env python

import requests
from io import BytesIO
from lxml import etree
import re

username = 'natas5'
password = 'Z0NsrtIkJoKALBCLi5eqFfcRN82Au2oD'

cookies = {"loggedin":"1"}

headers = {'Referer':'http://natas5.natas.labs.overthewire.org/'}

url = 'http://%s.natas.labs.overthewire.org' % username

session = requests.Session()
# print(session)

response = session.get(url,auth=(username,password),headers=headers,cookies=cookies)

content = response.text
print(content)
# print(content)
print(session.cookies)
# print(content)

# parser = etree.HTMLParser()
# content = etree.parse(BytesIO(content),parser=parser)
# for link in content.findall('//a'):
#     print(f'{link.get("url")}->{link.text}')