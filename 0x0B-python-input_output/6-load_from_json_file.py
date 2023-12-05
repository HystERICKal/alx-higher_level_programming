#!/usr/bin/python3
""" This fuction creates an Object from a “JSON file” """
import json


def load_from_json_file(filename):
    """ This fuction creates an Object from a “JSON file” """
    with open(filename) as the_file:
        return json.load(the_file)
