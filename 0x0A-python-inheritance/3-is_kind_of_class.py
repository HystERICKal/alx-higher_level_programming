#!/usr/bin/python3
""" Function returns true or false based on nature of object """


def is_kind_of_class(obj, a_class):
    """ Function returns true or false based on nature of object """
    if isinstance(obj, a_class):
        return True
    return False
