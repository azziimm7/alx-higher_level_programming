#!/usr/bin/python3

"""This module contains a function that convert a JSON to python object"""


from json import loads


def from_json_string(my_str):
    """Serialize a JSON to python object

    Args:
        my_str (str): The string we want to convert to python object
    """

    return (loads(my_str))
