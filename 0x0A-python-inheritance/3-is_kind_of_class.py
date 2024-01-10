#!/usr/bin/python3


"""

This module contains a function that tells if the
object is an instance of the specified class or if the
object is an instance of a class that inherited from, the specified class

"""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance of a specific class

    Args:
        obj (object): Any type of object can be passed
        a_class: Any class can be passed

    Returns:
        True if object is an instance of the specified class or if the
        object is an instance of a class that inherited from,
        the specified class; otherwise False.
    """

    return (isinstance(obj, a_class))
