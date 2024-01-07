#!/usr/bin/python3
"""

This module contains of a function that adds two integers only

"""


def add_integer(a, b=98):
    """

    Function that adds two integer and/or float numbers
    if the number is float it will be casted into integer

    Args:
        a: first number
        b: second number

    Returns:
        The addistion result

    Raises:
        TypeError: If a or b aren't integer and/or float numbers

    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
