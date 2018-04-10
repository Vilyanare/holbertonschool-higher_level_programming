#!/usr/bin/python3
'''
    Sends get requests to provided url and displays
    value for X-Request-ID header
'''
if __name__ == "__main__":
    import requests
    from sys import argv
    r = requests.get(argv[1])
    print(r.headers.get('x-request-id'))
