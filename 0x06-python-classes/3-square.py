#!/usr/bin/python3
"3-square.py define"


class Square:
    """ Class square
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        Area = self.__size * self.__size
        return Area
