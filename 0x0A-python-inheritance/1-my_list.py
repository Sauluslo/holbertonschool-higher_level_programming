#!/usr/bin/python3
""" class MyList that inherits from list
"""


class MyList(list):
    """ inherits from list
        Print list in order.
    """
    def __init__(self):
        pass
    
    def print_sorted(self):
        print(sorted(self))
