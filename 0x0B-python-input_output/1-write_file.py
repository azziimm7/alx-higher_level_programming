#!/usr/bin/python3

"""This module contains a function that writes texts to a file"""


def write_file(filename="", text=""):
    """Write text to a file

    Args:
        filename (str): The path to the file
        text (str): The content that will be written in the file

    Returns:
        The number of characters written

    """
    with open(filename, "w", encoding="UTF8") as f:
        char_nums = f.write(text)

    return char_nums
