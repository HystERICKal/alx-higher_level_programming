#!/usr/bin/python3
""" Function that writes a file """


def write_file(filename="", text=""):
    """ Function that writes a file """
    with open(filename, 'w+') as the_file:
        the_file.write(text)
    return len(text)
