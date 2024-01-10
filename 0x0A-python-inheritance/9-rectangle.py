#!/usr/bin/python3


"""A module defining the "Rectangle" class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        """
        Initialize an instance with only positive integer parameters

        Args:
            width (int): The width
            height (int): The height
        """

        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """ A user friendly representation of a rectangle"""

        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """Calculate the area of the rectangle"""

        return self.__width * self.__height
