#!/usr/bin/python3
""" This is the square class """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ This is the square class """
    def __init__(self, size):
        self.integer_validator('size', size)
        self.__size = size
        Rectangle.__init__(self, size, size)

    def area(self):
        return self.__size ** 2
