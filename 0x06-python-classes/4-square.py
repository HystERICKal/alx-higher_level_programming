#!/usr/bin/python3
"""This class defines a Square"""


class Square:
    """This class defines a Square"""

    def __init__(self, size=0):
        """The initialization of a brand new square.
        Args:
            size (none type): the new square is of this size.
        """
        self.size = size

    @property
    def size(self):
        """The Square's new size innit"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if (isinstance(value, int)):
            self.__size = value
            if value < 0:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')

    def area(self):
        """This determine's the square's area."""
        return (self.__size * self.__size)
