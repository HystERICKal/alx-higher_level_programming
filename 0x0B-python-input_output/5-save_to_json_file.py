#!/usr/bin/python3
""" Function that saves object to file """
import json


def save_to_json_file(my_obj, filename):
    """ Function that saves object to file """
    with open(filename, 'w+') as the_file:
        json.dump(my_obj, the_file)
