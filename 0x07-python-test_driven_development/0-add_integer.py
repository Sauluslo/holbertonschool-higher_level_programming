#!/usr/bin/python3
"0-add_integer.py - 0x07. Python - Test-driven development"


""" Methotd or function
    that adds 2 integers.
"""


def add_integer(a, b=98):
    """ Methotd or function
        that adds 2 integers.
    """
    if type(a) is int or type(a) is float:
        if type(b) is int or type(b) is float:
            return int(a) + int(b)
        else:
            raise TypeError("b must be an integer")
    else:
        raise TypeError("a must be an integer")
