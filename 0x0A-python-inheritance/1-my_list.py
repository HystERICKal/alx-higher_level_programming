#!/usr/bin/python3
"""This is the MyList Class"""


class MyList(list):
    """It inherits from list"""
    def print_sorted(self):
        """this prints the list...but sorted"""
        print(sorted(self))
