#!/usr/bin/python3
'''
    Contacts starwarsapi and requsts input value in the people search endpoint
'''
import requests
from sys import argv
r = requests.get('http://swapi.co/api/people/?search={}'.format(argv[1]))
swdict = r.json()
print('Number of results: {}'.format(swdict.get('count')))
for results in swdict.get('results'):
    print(results.get('name'))
