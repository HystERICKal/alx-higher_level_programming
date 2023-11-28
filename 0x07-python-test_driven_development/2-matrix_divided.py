#!/usr/bin/python3
"""Function Divides all matrix elements"""


def matrix_divided(matrix, div):
    """Function Divides all matrix elements"""

    matrx_len = len(matrix)
    check_inst = isinstance(matrix, list)
    v = 0
    if not check_inst or matrx_len == 0 or not matrix[0]:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    for i in matrix:
        row_len = len(i)
        if row_len == 0:
            raise TypeError(
                 "matrix must be a matrix (list of lists) of integers/floats")
        for j in i:
            if type(j) not in [int, float]:
                raise TypeError(
                    "matrix must be a " +
                    "matrix (list of lists) of integers/floats")

    the_rowlength = []
    for i in matrix:
        the_rowlength.append(len(i))
    check_not_all = [i == the_rowlength[0] for i in the_rowlength]
    if not all(check_not_all):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    final_matrx = []
    for j in matrix:
        temp = []
        for i in j:
            temp.append(round(i / div, 2))
        final_matrx.append(temp)

    return final_matrx
