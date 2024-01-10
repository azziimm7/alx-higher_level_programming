#!/usr/bin/python3


""" This module contains a function that tells if the
object is exactly an instance of the specified class"""


def is_same_class(obj, a_class):
    """Check if an object is an instance of a specific class

    Args:
        obj (object): Any type of object can be passed
        a_class: Any class can be passed

    Returns:
        True if object is exactly an instance of the specified class;
        otherwise False.
    """

    return type(obj) is a_class
