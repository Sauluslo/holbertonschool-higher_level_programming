#!/usr/bin/python3
""" 1-number_of_lines.py
"""


def number_of_lines(filename=""):
    """ Function that returns
        the number of lines of a text file:
    """
    with open(filename, 'r', encoding="utf-8") as file:
        return (len(file.readlines()))
