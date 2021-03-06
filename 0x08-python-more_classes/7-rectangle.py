#!/usr/bin/python3
""" 1-rectangle
"""


class Rectangle:
    """ class Rectangle that defines a rectangle by: (based on 0-rectangle.py)
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        promt = ""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            for width in range(self.__height - 1):
                promt += (str(self.print_symbol) * self.__width) + "\n"
            promt += (str(self.print_symbol) * self.__width)
            return promt

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.width, self.height))

    def area(self):
        Area = self.__width * self.__height
        return Area

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (2 * (self.height + self.width))

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """ Private instance attribute: height.
            property setter def height(self, value): to set it.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

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

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
