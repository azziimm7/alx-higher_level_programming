#!/usr/bin/python3

"""This module contains a function that writes texts to the end of a file"""


def append_write(filename="", text=""):
    """Write text at the end of a file

    Args:
        filename (str): The path to the file
        text (str): The content that will be written in the file

    Returns:
        The number of characters written

    """
    with open(filename, "a", encoding="UTF8") as f:
        char_nums = f.write(text)

    return char_nums
