#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):

    if len(matrix[0]) == 0:
        print("")
    else:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (i < len(matrix)) and (j < (len(matrix[0]) - 1)):
                    print("{}, ".format(matrix[i][j]), end='')
                else:
                    print("{}".format(matrix[i][j]))
