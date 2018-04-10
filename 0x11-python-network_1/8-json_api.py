#!/usr/bin/python3
'''
    Sends post request to http://0.0.0.0:5000/search_user with provided
    input and prints results with error handling
'''
if __name__ == "__main__":
    import requests
    from sys import argv
    q = ''
    if len(argv) > 1:
        q = argv[1]
    payload = {'q': q}
    r = requests.post('http://0.0.0.0:5000/search_user', data=payload)
    try:
        ids = r.json()
    except:
        print('Not a valid JSON')
        exit()
    if ids:
        print('[{}] {}'.format(ids.get('id'), ids.get('name')))
    else:
        print('No result')
