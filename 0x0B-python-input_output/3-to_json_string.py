#!/usr/bin/python3

"""This module contains a function that convert a python object to JSON"""


from json import dumps


def to_json_string(my_obj):
    """Serialize a python object to JSON

    Args:
        my_obj (object): The object we want to convert to JSON
    """

    return (dumps(my_obj))
