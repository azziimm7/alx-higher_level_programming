#!/usr/bin/python3

"""This module contains a function that convert a python object to JSON"""


from json import dump


def save_to_json_file(my_obj, filename):
    """

    Serialize a python object to JSON and write the result in a file

    Args:
        my_obj (object): The object we want to convert to JSON
        filename: The place were we will put the JSON string
    """

    with open(filename, "w", encoding="UTF8") as f:
        dump(my_obj, f)
