#!/usr/bin/python3
"""

This module contains of a function that adds two integers only

"""


def print_square(size):
    """

    Function that adds two integer and/or float numbers
    if the number is float it will be casted into integer

    Args:
        Size: The size of the square

    Returns:
        No returns

    Raises:
        TypeError: If a or b aren't integer and/or float numbers

    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
