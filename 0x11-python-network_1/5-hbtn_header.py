#!/usr/bin/python3
"""
anscript that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response.
"""
import requests
from sys import argv


if __name__ == "__main__":
    URL = argv[1]
    response = requests.get(URL)
    value = response.headers.get("X-Request-Id")
    print(value)
