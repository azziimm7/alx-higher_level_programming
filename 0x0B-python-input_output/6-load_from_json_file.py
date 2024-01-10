#!/usr/bin/python3

"""This module contains a function that Deserialize
a JSON file to a python object"""


from json import load


def load_from_json_file(filename):
    """

    Deserialize a JSON file to a python object

    Args:
        filename: The file containing the JSON string
    """

    with open(filename, "r", encoding="UTF8") as f:
        my_obj = load(f)

    return my_obj
