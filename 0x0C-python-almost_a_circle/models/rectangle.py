#!/usr/bin/python3
""" Class Base
"""
from models.base import Base


class Rectangle(Base):
    """ Class Rectangle that inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Init of the id in the class Rectangle
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ get the width in the class Rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ Private instance attribute: width.
            Property setter def width(self, value): to set it.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ get the height in the class Rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ Private instance attribute: height.
            Property setter def height(self, value): to set it.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """ get the x in the class Rectangle
        """
        return self.__x

    @x.setter
    def x(self, value):
        """ Private instance attribute: x.
            Property setter def x(self, value): to set it.
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """ get the y in the class Rectangle
        """
        return self.__y

    @y.setter
    def y(self, value):
        """ Private instance attribute: y.
            Property setter def y(self, value): to set it.
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """ Return area of a rentangle
        """
        area = self.__width * self.__height
        return area

    def display(self):
        """ That prints in stdout the Rectangle
            instance with the character # - you
            don’t need to handle x and y here.
        """
        print("\n" * self.y, end="")
        for height in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        a, d, e = self.id, self.width, self.height
        b, c = self.x, self.y
        return "[Rectangle] ({}) {}/{} - {}/{}".format(a, b, c, d, e)
