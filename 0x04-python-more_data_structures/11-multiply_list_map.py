#!/usr/bin/python3
""" function that returns a list with all
    values multiplied by a number without using any loops.
"""


def multiply_list_map(my_list=[], number=0):
    """ (1) Returns a new list:
        (2) Same length as my_list
        (3) Each value should be multiplied by number
        (4) Initial list should not be modified
        (5) You are not allowed to import any module
        (6) You have to use map
        (7) Your file should be max 3 lines
    """
    return (list(map(lambda x: x * number, my_list)))
