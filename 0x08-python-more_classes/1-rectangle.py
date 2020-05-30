#!/usr/bin/python3
""" 1-rectangle
"""

class Rectangle:
    """ class Rectangle that defines a rectangle by: (based on 0-rectangle.py)
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height


    @property
    def width(self):
        return self.__width


    @width.setter
    def width(self, value):
        """ Private instance attribute: width.
            Property setter def width(self, value): to set it.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value


    @property
    def height(self):
        return self.__height


    @height.setter
    def height(self, value):
        """ Private instance attribute: height.
            property setter def height(self, value): to set it.
        """


        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__height = value