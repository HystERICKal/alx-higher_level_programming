#!/usr/bin/python3
"""
This is a Rectangle class
"""


class Rectangle:
    """The Rectangle class with added functionality"""

    def __init__(self, width=0, height=0):
        """Constructor of Rectangle class"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Private instance of attribute width retrieved here"""
        return self.__width

    @width.setter
    def width(self, value):
        """Private instance of attribute width is set here"""
        if isinstance(value, int):
            self.__width = value
            if value < 0:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """Private instance of attribute height retrieved here"""
        return self.__height

    @height.setter
    def height(self, value):
        """Private instance of attribute height is set here"""
        if isinstance(value, int):
            self.__height = value
            if value < 0:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")
