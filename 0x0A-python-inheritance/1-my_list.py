#!/usr/bin/python3


"""A module defining a class that inherits from the list class"""


class MyList(list):
    """A class that inherits the list properties"""

    def print_sorted(self):
        """Print the sorted list without changing its content"""

        print(sorted(self))
