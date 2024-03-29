#!/usr/bin/python3
"""
a script that fetches https://alx-intranet.hbtn.io/status
"""
import requests


if __name__ == "__main__":
    """ main """

    URL = "https://alx-intranet.hbtn.io/status"
    response = requests.get(URL)
    content = response.text
    print('Body response:')
    print('\t- type: {}'.format(type(content)))
    print('\t- content: {}'.format(content))
