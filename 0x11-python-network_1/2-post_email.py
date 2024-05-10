#!/usr/bin/python3
""" A script takes the URL and email, and sends a POST request
to the person it was passed to"""


if __name__ == '__main__':
    import sys
    import urllib.parse
    import urllib.request

    data = urllib.parse.urlencode({'email': sys.argv[2]})
    data = data.encode('utf-8')
    request = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode(encoding='utf-8'))
