#!/usr/bin/python3
""" a Python script that takes in a URL, sends
a request to the URL and displays the value of the X-Request-Id
variable found in the header of the response. """
from urllib.request import urlopen
from sys import argv

if __name__ == "__main__":
    """ a Python script that fetches URLs"""

    URL = argv[1]
    with urlopen(URL) as response:
        html = response.info()
        value = html.get('X-Request-Id')
        print(value)
