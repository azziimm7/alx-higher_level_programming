#!/usr/bin/python3

"""This module contains a class called Student"""


class Student:
    """A student class"""

    def __init__(self, first_name, last_name, age):
        """Inintialze a student object

        Args:
            first_name (str): The student's first name
            last_name (str): The student's last name
            age (int): The student's age

        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Create a JSON representation for Student objects"""

        json = {"first_name": self.first_name, "last_name": self.last_name,
                "age": self.age}
        return json
