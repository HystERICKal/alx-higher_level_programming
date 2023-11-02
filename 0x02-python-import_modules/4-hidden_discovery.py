#!/usr/bin/python3
import hidden_4

if __name__ == '__main__':
    the_names = dir(hidden_4)
    sorted_list = sorted(the_names)
    len_of_sorted_list = len(sorted_list)

    for p in range(len_of_sorted_list):
        if sorted_list[p][0] != '_':
            print(sorted_list[p])
