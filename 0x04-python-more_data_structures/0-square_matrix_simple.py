#!/usr/bin/python3
""" A Function that computes
    the square value of all integers of a matrix.
"""


def square_matrix_simple(matrix=[]):
    if matrix:
        new_matrix = []
        for rows in matrix:
            new_matrix.append([n ** 2 for n in rows])
        return new_matrix
