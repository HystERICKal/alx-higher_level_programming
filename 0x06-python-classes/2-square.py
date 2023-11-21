#!/usr/bin/python3
"""This class defines a Square"""


class Square:
    """This class defines a Square"""

    def __init__(self, size=0):
        """The initialization of a brand new square.
        Args:
            size (none type): the new square is of this size.
        """
        if (isinstance(size, int)):
            self.__size = size
            if size < 0:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')
