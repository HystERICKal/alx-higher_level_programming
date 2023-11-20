#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    ints_printed_count = 0
    v = 0
    while v < x:
        try:
            print('{:d}'.format(my_list[v]), end='')
            ints_printed_count = ints_printed_count + 1
        except (TypeError, ValueError):
            pass
        v += 1
    print()
    return ints_printed_count
