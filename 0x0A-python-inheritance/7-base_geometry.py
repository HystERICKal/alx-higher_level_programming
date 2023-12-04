#!/usr/bin/python3
""" This is the class BaseGeometry """


class BaseGeometry:
    """ This is the class BaseGeometry """
    def area(self):
        """This Function raises an exception"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """This function validated value"""
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
