#!/usr/bin/python3
"""Python bytecode"""
import math


class MagicClass:
    """The MagicClass Class"""
    def __init__(self, radius=0):
        """the constructor of the magic class"""
        self._MagicClass__radius = 0
        if type(radius) is not int:
            raise TypeError("radius must be a number")
        elif type(radius) is not float:
            raise TypeError("radius must be a number")
        self._MagicClass__radius = radius

    def area(self):
        """The area of the magic class"""
        return self._MagicClass__radius * self._MagicClass__radius * math.pi

    def circumference(self):
        """The circumference of the magic class"""
        return 2 * math.pi * self._MagicClass__radius
