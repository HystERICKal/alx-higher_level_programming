#!/usr/bin/python3
""" Returns true or false based on nature of object """


def inherits_from(obj, a_class):
    """ Returns true or false based on nature of object """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
