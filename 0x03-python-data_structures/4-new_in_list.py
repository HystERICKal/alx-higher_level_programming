#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    the_new_lst = list(my_list)  # copy to new list
    the_new_lst[idx] = element  # replace element
    return the_new_lst
