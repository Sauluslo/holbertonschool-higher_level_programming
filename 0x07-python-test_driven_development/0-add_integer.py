#!/usr/bin/python3
"0-add_integer.py - 0x07. Python - Test-driven development"


""" Methotd or function
    that adds 2 integers.
"""


def add_integer(a, b=98):
    if type(a) is int or type(a) is float:
        if type(b) is int or type(b) is float:
            return int(a) + int(b)
        else:
            raise ValueError("b must be an integer")
    else:
        raise ValueError("a must be an integer")
