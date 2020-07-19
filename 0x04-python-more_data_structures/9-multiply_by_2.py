#!/usr/bin/python3
""" A Function that returns a new dictionary
    with all values multiplied by 2.
"""


def multiply_by_2(a_dictionary):
    """ (1) You can assume that all values are only integers
        (2) Returns a new dictionary
        (3) You are not allowed to import any module
    """
    new_dict = a_dictionary.copy()
    for key in new_dict:
        new_dict[key] *= 2
    return new_dict
