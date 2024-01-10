#!/usr/bin/python3


"""A module defining the "BaseGeometry" class"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Raise an exception if the method is called

        Raises:
            Exception: If the method is called
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Check if value is positive integer

        Args:
            name (str): The name of the value we want to check
            value (object): The instance we want to validate

        Raises:
            TypeError: If the value is not an integer
            ValueError: If value is less than or equals zero
        """

        if (type(value) is not int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
