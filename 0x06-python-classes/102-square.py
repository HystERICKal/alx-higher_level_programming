#!/usr/bin/python3
"""This is the Square"""


class Square:
    """The body of the square"""

    def __init__(self, size=0):
        """The constructore of the square"""
        self.__size = size

    @property
    def size(self):
        """"The size property of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self.__size = value
            if value < 0:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')

    def area(self):
        """This returnscurrent square area"""
        return self.__size * self.__size

    def __le__(self, the_num):
        """less than or equal to"""
        return self.area() <= the_num.area()

    def __lt__(self, the_num):
        """less than"""
        return self.area() < the_num.area()

    def __ge__(self, the_num):
        """greater than or equal to"""
        return self.area() >= the_num.area()

    def __ne__(self, the_num):
        """ not equal to"""
        return self.area() != the_num.area()

    def __gt__(self, the_num):
        """greater than"""
        return self.area() > the_num.area()

    def __eq__(self, the_num):
        """equal to"""
        return self.area() == the_num.area()
