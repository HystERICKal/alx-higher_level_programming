#!/usr/bin/python3
""" Function that returns true or false based on the object's nature """


def is_same_class(obj, a_class):
    """ Function that returns true or false based on the object's nature """
    if type(obj) is a_class:
        return True
    return False
