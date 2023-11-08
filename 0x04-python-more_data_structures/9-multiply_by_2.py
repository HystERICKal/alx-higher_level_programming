#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    the_double_dict = a_dictionary.copy()
    for d in the_double_dict:
        the_double_dict[d] = the_double_dict[d] * 2
    return the_double_dict
