#!/usr/bin/python3

"""A module containing the Rectangle class"""

from models.base import Base


class Rectangle(Base):
    """
    A Rectangle class

    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the class with a specific id

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
            x (int): The x coordinate of the rectangle
            y (int): The y coordinate of the rectangle
            id (int): The rectangle's id

        Raises:
            TypeError: If any of the attributes is not an int
            ValueError: If either width or height is <= 0
            ValueError: If either x or y is < 0

        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def height(self):
        """Set/get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def width(self):
        """Set/get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def x(self):
        """Set/get the x coordinate of the rectangle"""
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Set/get the y coordinate of the rectangle"""
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Return the area of the rectangle"""

        return self.width * self.height

    def display(self):
        """Print the rectangle using the '#' character"""

        [print() for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print()

    def __str__(self):
        """Return a user friendly string representation of the rectangle"""

        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """Update the rectangle attributes

        Args:
            *args (ints): New values for attributes
                - 1st argument represents the id attribute
                - 2nd argument represents the width attribute
                - 3rd argument represents the height attribute
                - 4th argument represents the x attribute
                - 5th argument represents the y attribute
            **kwargs (dict): A dict containing the new key/val pairs
        """
        if args and len(args) != 0:
            for i, arg in enumerate(args):
                if i == 0 and arg is None:
                    self.__init__(self.width, self.height, self.x, self.y)
                elif i == 0:
                    self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg

        elif kwargs and len(kwargs) != 0:
            for key, val in kwargs.items():
                if key == "id" and val is None:
                    self.__init__(self.width, self.height, self.x, self.y)
                elif key == "id":
                    self.id = val
                elif key == "width":
                    self.width = val
                elif key == "height":
                    self.height = val
                elif key == "x":
                    self.x = val
                elif key == "y":
                    self.y = val

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle"""
        return {
                'id': self.id,
                'height': self.height,
                'width': self.width,
                'x': self.x,
                'y': self.y
                }
