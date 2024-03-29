#!/usr/bin/python3
""" a Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as
a parameter, and displays the body of the response
(decoded in utf-8) """

from sys import argv
from urllib import request, parse


if __name__ == '__main__':
    """main"""

    URL = argv[1]
    value = {'email': argv[2]}

    data = parse.urlencode(value).encode('ascii')
    req = request.Request(URL, data)

    with request.urlopen(req) as response:
        html = response.read()
        print(html.decode('utf-8'))
