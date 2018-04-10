#!/usr/bin/python3
'''
    Sends get request to https://intranet.hbtn.io/status and displays info
'''
import requests
r = requests.get('https://intranet.hbtn.io/status')
print('''Body response:
    - type: {}
    - content: {}'''.format(type(r.text), r.text))
