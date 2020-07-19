#!/usr/bin/python3
""" A Function that returns a key
    with the biggest integer value.
"""


def best_score(a_dictionary):
    """ (1) You can assume that all values are only integers.
        (2) If no score found, return None.
        (3) You can assume all students have a different score.
        (4) You are not allowed to import any module.
    """
    if a_dictionary is not None:
        best_score = max(a_dictionary, key=a_dictionary.get)
        return best_score
