#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    elem_printed = 0
    for v in range(x):
        try:
            print('{}'.format(my_list[v]), end='')
            elem_printed = elem_printed + 1
        except IndexError:
            pass
    print()
    return elem_printed
