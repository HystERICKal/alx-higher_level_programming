#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple_a = tuple_manipulation(tuple_a)
    new_tuple_b = tuple_manipulation(tuple_b)
    return (new_tuple_a[0] + new_tuple_b[0], new_tuple_a[1] + new_tuple_b[1])


def tuple_manipulation(tuple_x):
    if len(tuple_x) < 2:
        if len(tuple_x) == 0:
            tuple_x = 0, 0
            return tuple_x
        else:
            tuple_x = tuple_x[0], 0
            return tuple_x
    else:
        return tuple_x
