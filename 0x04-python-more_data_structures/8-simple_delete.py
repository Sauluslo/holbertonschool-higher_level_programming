#!/usr/bin/python3
"""
"""


def simple_delete(a_dictionary, key=""):
    """ (1) key argument will be always a string
        (2) If a key doesn’t exist, the dictionary won’t change
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
