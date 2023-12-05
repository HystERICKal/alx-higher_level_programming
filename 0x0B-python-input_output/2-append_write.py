#!/usr/bin/python3
""" Function that appends to a file """


def append_write(filename="", text=""):
    """ Function that appends to a file """
    with open(filename, 'a+') as the_file:
        the_file.write(text)
    return len(text)
