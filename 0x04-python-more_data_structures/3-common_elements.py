#!/usr/bin/python3
""" A Function that returns a set
    of common elements in two sets.
"""


def common_elements(set_1, set_2):
    element = list(set(set_1).intersection(set_2))
    return element
