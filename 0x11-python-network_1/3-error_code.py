#!/usr/bin/python3
'''
    Requests body of information from provided url but handles HTTP errors
'''
if __name__ == "__main__":
    from sys import argv
    import urllib.request

    req = urllib.request.Request(argv[1])
    try:
        html = urllib.request.urlopen(req)
        print(html.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
