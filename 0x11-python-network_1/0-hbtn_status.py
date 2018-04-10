#!/usr/bin/python3
'''
    Prints information about the page intranet.hbtn.io/status
'''
if __name__ == "__main__":
    import urllib.request
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
    print('''Body response:
        - type:{}
        - content:{}
        - utf8 content:{}'''.format(type(html), html, html.decode('utf-8')))
