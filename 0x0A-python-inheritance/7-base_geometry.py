#!/usr/bin/python3
""" Class BaseGeometry (based on 6-base_geometry.py).
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

    def integer_validator(self, name, value):
        """ Public instance method:
            def integer_validator(self, name, value):
            that validates value
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        else:
            return value
