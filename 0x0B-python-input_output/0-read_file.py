#!/usr/bin/python3

"""This module contains a function that prints the content of a file"""


def read_file(filename=""):
    """Read the file content and print it out

    Args:
        filename (str): The path to the file
    """
    with open(filename, "r", encoding="UTF8") as f:
        file_content = f.read()

    print(file_content, end="")
