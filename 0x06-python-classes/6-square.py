#!/usr/bin/python3
"""This class defines a Square"""


class Square:
    """This class defines a Square"""

    def __init__(self, size=0, position=(0, 0)):
        """The initialization of a brand new square.
        Args:
            size (none type): the new square is of this size.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """The square's new position."""
        return (self.__position)

    @position.setter
    def position(self, digit):
        if isinstance(digit[0], int):
            if digit[0] >= 0 and digit[1] >= 0:
                self.__position = digit
        elif isinstance(digit[1], int):
            if digit[0] >= 0 and digit[1] >= 0:
                self.__position = digit
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """This determine's the square's area."""
        return (self.__size * self.__size)

    def my_print(self):
        """This one prints a square with #"""
        x = 0
        y = 0
        z = 0
        w = 0

        while z < self.__position[1]:
            print("")
            z += 1

        while x < self.__size:
            for w in range(self.__position[0]):
                print(" ", end="")
            for y in range(self.__size):
                print("#", end="")
            print("")
            x += 1
        if self.__size == 0:
            print("")
            return
