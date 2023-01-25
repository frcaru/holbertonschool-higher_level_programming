#!/usr/bin/python3


def squarevalue(value):

    value = value ** 2
    return value


def square_matrix_simple(matrix=[]):

    if not matrix:
        return None
    new_matrix = []
    value = ""

    for i in matrix:
        value = map(squarevalue, matrix[matrix.index(i)])
        new_matrix.append(list(value))

    return new_matrix
