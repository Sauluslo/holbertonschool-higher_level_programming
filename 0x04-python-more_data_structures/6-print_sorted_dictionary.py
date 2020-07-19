#!/usr/bin/python3
""" A Function that prints
    a dictionary by ordered keys.
"""


def print_sorted_dictionary(a_dictionary):
    sort_key = a_dictionary.keys()
    for key in sorted(sort_key):
        print("{}: {}".format(key, a_dictionary[key]))
