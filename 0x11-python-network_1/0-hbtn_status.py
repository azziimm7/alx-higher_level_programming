#!/usr/bin/python3
""" This module shows the body responceof url """
from urllib.request import urlopen

if __name__ == "__main__":
    """ a Python script that fetches
    https://alx-intranet.hbtn.io/status """

    URL = "https://alx-intranet.hbtn.io/status"
    with urlopen(URL) as response:
        html = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(html)))
        print('\t- content: {}'.format(html))
        print('\t- utf8 content: {}'.format(html.decode("utf-8")))
