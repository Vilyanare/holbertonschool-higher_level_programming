#!/usr/bin/python3
'''
    Sends a post to provided url with provided email address as email value
'''
if __name__ == "__main__":
    import requests
    from sys import argv

    payload = {'email': argv[2]}
    r = requests.post(argv[1], data=payload)
    print(r.text)
