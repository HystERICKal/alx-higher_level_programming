#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    second_dict = a_dictionary.copy()
    for the_key, the_val in second_dict.items():
        if value == the_val:
            a_dictionary.pop(the_key)
    return a_dictionary
