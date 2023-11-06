#!/usr/bin/python3
def no_c(my_string):
    fomatted_string = ""
    for remove_letter in my_string:
        if remove_letter != "c" and remove_letter != "C":
            fomatted_string = fomatted_string + remove_letter
    return fomatted_string
