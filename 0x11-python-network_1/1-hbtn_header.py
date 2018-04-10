#!/usr/bin/python3
'''
    Finds the value for the header X-Request-Id in the provided URL
'''
import urllib.request
from sys import argv
with urllib.request.urlopen(argv[1]) as response:
    for x in response.headers.__dict__.get('_headers'):
        if x[0] == 'X-Request-Id':
            print(x[1])
