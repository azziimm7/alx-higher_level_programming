#!/usr/bin/python3
"""
a script that takes in a URL and an email, sends a POST request to
the passed URL with the email as a parameter, and displays the
body of the response.
"""
import requests
from sys import argv


if __name__ == "__main__":
    """ main """

    URL = argv[1]
    email = argv[2]
    value = {"email": email}
    response = requests.post(URL, data=value)
    print(response.text)
