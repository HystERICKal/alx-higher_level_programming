#!/usr/bin/python3
""" The technical interview """


def pascal_triangle(n):
    """The pascal triangle function"""
    list1 = []
    list2 = []
    x = 0
    if not n <= 0:
        while x < n:
            list2.append(x + 1)
            list1.append(list2)
            x += 1
    return list1
