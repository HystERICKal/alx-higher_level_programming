#!/usr/bin/python3
"""This function adds 2 ints"""


def add_integer(a, b=98):
    """This function adds 2 ints"""

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    result = int(a) + int(b)
    return result
