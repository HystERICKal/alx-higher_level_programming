#!/usr/bin/python3
"""Function prints first and last name"""


def say_my_name(first_name, last_name=""):

    """Function prints first and last name"""

    check_firstname = isinstance(first_name, str)
    check_secondname = isinstance(last_name, str)

    if not check_firstname:
        raise TypeError('first_name must be a string')
    if not check_secondname:
        raise TypeError('last_name must be a string')
    if first_name is None:
        first_name = ''
    print('My name is {} {}'.format(first_name, last_name))
