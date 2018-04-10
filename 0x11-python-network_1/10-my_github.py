#!/usr/bin/python3
'''
'''
from sys import argv
import requests
r = requests.get('https://api.github.com/user', auth=(argv[1], argv[2]))
print(r.json().get('id'))
