#!/usr/bin/python3

"""A module containing the Base class for all next
implemented classes"""

import json


class Base:
    """

    A base class for other classes like
    Rectangle and Square classes

    Args:
        __nb_objects (int): The number of base class objects

    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the class with a specific id

        Args:
            id (int): The object's id

        """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of a list of dictionaries

        Args:
            list_dictionaries (list): A list of dictionaries

        Returns:
            The JSON string representation
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file

        Args:
            list_objs (list): a list of instances who inhertis of Base
        """
        if list_objs is not None:
            json_list = [obj.to_dictionary() for obj in list_objs]
        else:
            json_list = []

        with open(f"{cls.__name__}.json", "w", encoding="UTF8") as f:
            f.write(Base.to_json_string(json_list))
