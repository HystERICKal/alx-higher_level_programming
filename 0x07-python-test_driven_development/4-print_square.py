#!/usr/bin/python3
""" Function prints a square with # """


def print_square(size):
    """ Function prints a square with # """

    x = 0

    if size < 0:
        raise ValueError('size must be >= 0')

    check_size_fl = isinstance(size, float)
    check_size_in = isinstance(size, int)

    if check_size_fl and size < 0:
        raise TypeError('size must be an integer')
    if not check_size_in:
        raise TypeError('size must be an integer')

    while x < size:
        for y in range(size):
            print('#', end='')
        print()
        x += 1
