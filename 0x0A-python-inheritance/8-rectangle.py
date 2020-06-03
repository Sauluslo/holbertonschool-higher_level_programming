#!/usr/bin/python3
""" class Rectangle that inherits
    from BaseGeometry (7-base_geometry.py)
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Inherits from BaseGeometry.
    """
    def __init__(self, width, height):
        """ Inicialize attributes.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
