#!/usr/bin/python3


"""

This module contains a function that tells if the
object is an instance of a class
that inherits from a specific class(directly or indirectly)

"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class
    that inherits from a specific class(directly or indirectly)

    Args:
        obj (object): Any type of object can be passed
        a_class: Any class can be passed

    Returns:
        True if object is an instance of a class that
        inherited from the specific class; otherwise False.
    """

    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
