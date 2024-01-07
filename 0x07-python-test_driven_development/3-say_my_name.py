#!/usr/bin/python3
"""

This module contains of a function that will print the name of a person

"""


def say_my_name(first_name, last_name=""):
    """

    Function that prints the name of a person

    Args:
        first_name (string): The first name of the person
        last_name (string): The last name of the person

    Raises:
        TypeError: If the first_name and/or last_name isn't a string

    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
