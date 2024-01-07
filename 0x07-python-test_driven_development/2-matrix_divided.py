#!/usr/bin/python3
"""

This module contains of a function that divides a list of
lists by a specific value.

"""


def matrix_divided(matrix, div):
    """

    Function that divides all elements of a matrix

    Args:
        matrix (list): A list of lists of integers and/or floats
        div (int/float): The division number

    Returns:
        A new matrix containing the division result
        rounded to 2 decimal places

    Raises:
        TypeError: If matrix isn't a list of lists of integers or floats.
        TypeError: If the rows of the matrix aren't of the same size.
        TypeError: If div isn't an integer or float
        ZeroDivisionError: If div equals zero

    """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    err_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(ele, (int, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError(err_msg)

    row_len = len(matrix[0])
    if not all(len(row) == row_len for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    result = [[round((item / div), 2) for item in row] for row in matrix]
    return result
