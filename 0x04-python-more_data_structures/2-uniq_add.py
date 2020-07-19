#!/usr/bin/python3
"""
"""


def uniq_add(my_list=[]):
    set_list = set(my_list)
    sum_list = 0
    for item in set_list:
        sum_list += item
    return sum_list
