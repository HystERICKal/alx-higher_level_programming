#!/usr/bin/python3

""" function returns object repped by JSON string """
import json


def from_json_string(my_str):
    """ function returns object repped by JSON string """

    return json.loads(my_str)
