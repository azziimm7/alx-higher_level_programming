#!/usr/bin/python3
"""
 a Python script that takes in a letter and sends a POST request to
 http://0.0.0.0:5000/search_user with the letter as a parameter
"""
from sys import argv
import requests


if __name__ == "__main__":
    """ main """

    URL = "http://0.0.0.0:5000/search_user"
    c = ""
    if len(argv) > 1:
        c = {"q": argv[1][0]}
    req = requests.post(URL, data=c)
    try:
        res = req.json()
        if res:
            str_re = "[{}] {}"
            print(str_re.format(res.get("id"), res.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
