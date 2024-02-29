#!/usr/bin/python3
"""tech interview finding a peak"""


def find_peak(list_of_integers):
    """tech interview finding a peak"""
    temp_list = list_of_integers
    temp_list_len = len(temp_list)
    if temp_list_len == 0:
        return
    no_rem = temp_list_len // 2
    if (no_rem == temp_list_len - 1 or temp_list[no_rem] >=
        temp_list[no_rem + 1]) and (no_rem == 0 or
                                    temp_list[no_rem] >=
                                    temp_list[no_rem - 1]):
        return temp_list[no_rem]
    if (no_rem != temp_list_len - 1 and
            temp_list[no_rem + 1] > temp_list[no_rem]):
        return find_peak(temp_list[no_rem + 1:])
    return find_peak(temp_list[:no_rem])
