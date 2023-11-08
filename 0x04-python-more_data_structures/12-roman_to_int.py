#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return 0
    the_roman_reference = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    outer = []
    for s in roman_string:
        outer.append(the_roman_reference[s])
    final_int = 0
    i = 0
    while i < len(outer):
        final_int = final_int + outer[i]
        if outer[i - 1] < outer[i] and i != 0:
            final_int = final_int - (outer[i - 1] + outer[i - 1])
        i = i + 1
    return final_int
