#!/usr/bin/python3
'''
    Sends a post request to given website with given email
    address as email value
'''
if __name__ == "__main__":
    from sys import argv
    import urllib.parse
    import urllib.request
    url = argv[1]
    values = {'email': argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        the_page = response.read().decode('utf-8')
    print(the_page)
