#!/usr/bin/python3
import json
""" function returns object repped by JSON string """


def from_json_string(my_str):
    """ function returns object repped by JSON string """

    return json.loads(my_str)
