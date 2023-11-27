#!/usr/bin/python3
"""
This is a Rectangle class
"""


class Rectangle:
    """The Rectangle class with added functionality"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Constructor of Rectangle class"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances = Rectangle.number_of_instances + 1

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

    def area(self):
        """Rectangle Area is returned"""
        return self.__width * self.__height

    def perimeter(self):
        """Rectangle Perimeter is returned"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height + self.__width + self.__height)

    def __str__(self):
        """String Representation"""
        if self.__width == 0 or self.__height == 0:
            return ''
        temp_str = ''
        i = 0
        while i < self.__height:
            for j in range(self.__width):
                temp_str = temp_str + '#'
            temp_str = temp_str + '\n'
            i += 1
        return temp_str[:-1]

    def __repr__(self):
        """Rectangle String representation"""
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """Rectangle instance gets deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances = Rectangle.number_of_instances - 1
