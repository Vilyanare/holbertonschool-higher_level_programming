#!/usr/bin/python3
'''
    Sends a get request to provided url but handles HTTP errors
'''
if __name__ == "__main__":
    from sys import argv
    import requests

    r = requests.get(argv[1])
    try:
        r.raise_for_status()
        print(r.text)
    except requests.exceptions.HTTPError as e:
        print('Error code: {}'.format(e.response.status_code))
