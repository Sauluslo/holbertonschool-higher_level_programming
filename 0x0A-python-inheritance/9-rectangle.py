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
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """ Representation Informal of a Rectangle
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def __repr__(self):
        """ Representation formal of a Rectangle
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        return self.__width * self.__height
