#!/usr/bin/python3


"""A module defining the "Square" class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """
        Initialize an instance with only positive integer parameters

        Args:
            size (int): The size
        """

        super().integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """ A user friendly representation of a square"""

        return f"[Square] {self.__size}/{self.__size}"

    def area(self):
        """Calculate the area of the square"""

        return self.__size ** 2
