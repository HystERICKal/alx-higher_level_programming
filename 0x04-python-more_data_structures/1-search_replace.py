#!/usr/bin/python3
def search_replace(my_list, search, replace):
    update_list = []
    x = 0
    while x < len(my_list):
        if my_list[x] == search:
            update_list.append(replace)
        else:
            update_list.append(my_list[x])
        x += 1
    return update_list
