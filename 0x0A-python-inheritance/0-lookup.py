#!/usr/bin/python3


""" This module contains a function to return thr list of
available attributes and methods of an object"""


def lookup(obj):
    """ Find the list of available attributes and methods of an object

    Args:
        obj (object): Any type of object can be passed

    Returns:
        The  list of available attributes and methods of an object
    """
    return (dir(obj))
