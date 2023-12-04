#!/usr/bin/python3
"""Function adds new attributes"""


def add_attribute(obj, the_attribute, the_value):
    """Function adds new attributes"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, the_attribute, the_value)
