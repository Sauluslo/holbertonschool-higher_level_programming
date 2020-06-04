#!/usr/bin/python3
""" 0-read_file.py
"""


def read_file(filename=""):
    """ Function that reads a text file
        (UTF8) and prints it to stdout:
    """
    with open(filename, 'r') as file:
        read_data = file.read()
        print(read_data, end="")
