#!/usr/bin/python3


"""A module defining an improved version of "BaseGeometry" class"""


class BaseGeometry:
    """An improved version of BaseGeometry class"""

    def area(self):
        """Raise an exception if the method is called

        Raises:
            Exception: If the method is called
        """
        raise Exception("area() is not implemented")
