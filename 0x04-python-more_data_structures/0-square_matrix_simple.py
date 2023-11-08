#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared = []
    for line in matrix:
        the_row = []
        for c in line:
            the_row.append(c**2)
        squared.append(the_row)
    return squared
