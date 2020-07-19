#!/usr/bin/python3
""" A Function that replaces or
    adds key/value in a dictionary.
"""


def update_dictionary(a_dictionary, key, value):
    """ (1) key argument will be always a string.
        (2) value argument will be any type.
        (3) If a key exists in the dictionary,
        the value will be replaced.
        (4) If a key doesn’t exist in the dictionary,
        it will be created.
        (5) You are not allowed to import any module.
    """
    a_dictionary[key] = value
    return a_dictionary
