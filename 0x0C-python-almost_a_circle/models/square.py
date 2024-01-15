#!/usr/bin/python3

"""A module containing the Square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A square class

    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the class with a specific id

        Args:
            size (int): The size of the square
            x (int): The x coordinate of the square
            y (int): The y coordinate of the square
            id (int): The square's id

        Raises:
            TypeError: If any of the attributes is not an int
            ValueError: If either width or height is <= 0
            ValueError: If either x or y is < 0

        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Set/get the size of the square"""
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def __str__(self):
        """Return a user friendly string representation of the square"""

        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y,
                                                 self.size)

    def update(self, *args, **kwargs):
        """Update the square attributes

        Args:
            *args (ints): New values for attributes
                - 1st argument represents the id attribute
                - 2nd argument represents the size attribute
                - 3th argument represents the x attribute
                - 4th argument represents the y attribute
            **kwargs (dict): A dict containing the new key/val pairs
        """
        if args and len(args) != 0:
            for i, arg in enumerate(args):
                if i == 0 and arg is None:
                    self.__init__(self.size, self.x, self.y)
                elif i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg

        elif kwargs and len(kwargs) != 0:
            for key, val in kwargs.items():
                if key == "id" and val is None:
                    self.__init__(self.size, self.x, self.y)
                elif key == "id":
                    self.id = val
                elif key == "size":
                    self.size = val
                elif key == "x":
                    self.x = val
                elif key == "y":
                    self.y = val

    def to_dictionary(self):
        """Return the dictionary representation of a square"""
        return {
                'id': self.id,
                'size': self.width,
                'x': self.x,
                'y': self.y
                }
