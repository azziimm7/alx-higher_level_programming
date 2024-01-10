#!/usr/bin/python3

"""This module contains a function that returns the
dictionary description of an object"""


def class_to_json(obj):
    """

    Return the dictionary description with
    simple data structure (list, dictionary, string,
    integer and boolean) for JSON serialization of an object

    Args:
        obj: The file containing the JSON string

    Returns:
        The the dictionary description
    """

    return obj.__dict__
