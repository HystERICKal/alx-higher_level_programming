#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    bigspace = ' '
    nospace = ''
    for e in range(len(matrix)):
        for f in range(len(matrix[e])):
            if f != len(matrix[e]) - 1:
                print('{:d}'.format(matrix[e][f]), end=bigspace)
            else:
                print('{:d}'.format(matrix[e][f]), end=nospace)
        print()
