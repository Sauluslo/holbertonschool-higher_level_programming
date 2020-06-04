#!/usr/bin/python3
""" 1-number_of_lines.py
"""


def read_lines(filename="", nb_lines=0):
    """ Function that returns
        the number of lines of a text file:
    """
    with open(filename, 'r', encoding="utf-8") as file:
        if nb_lines <= 0:
            print(file.read(), end="")
        else:
            line = "".join(file.readlines()[:nb_lines])
            print(line, end="")
