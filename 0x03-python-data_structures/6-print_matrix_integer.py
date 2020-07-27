#!/usr/bin/python3
""" Function that prints a matrix of integers.
"""


def print_matrix_integer(matrix=[[]]):
    if len(matrix[0]) is 0:
        print()

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j != len(matrix[i]) - 1:
                print("{:d}".format(matrix[i][j]), end=" ")
            else:
                print("{:d}".format(matrix[i][j]))
