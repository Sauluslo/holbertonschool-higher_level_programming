#!/usr/bin/python3
"""find peak in a list"""


def find_peak(list_of_integers):
    """return the peak"""
    length = len(list_of_integers)
    if length == 0:
        return None
    list_of_integers.sort()
    return list_of_integers[-1]
