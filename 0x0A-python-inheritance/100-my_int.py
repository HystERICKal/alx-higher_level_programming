#!/usr/bin/python3
"""This is the MyInt class"""


class MyInt(int):
    """And it is a rebel"""

    def __eq__(self, value):
        return self.real != value

    def __ne__(self, value):
        return self.real == value
