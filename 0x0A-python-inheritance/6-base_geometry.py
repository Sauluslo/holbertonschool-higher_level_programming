#!/usr/bin/python3
""" Class BaseGeometry (based on 5-base_geometry.py).
"""


class BaseGeometry:
    """ Public instance method: def area(self):
        that raises an Exception with the message:
        area() is not implemented
    """
    def __init__(self):
        pass

    def area(self):
        raise Exception("area() is not implemented")
