#!/usr/bin/python3
"4-square.py define"


class Square:
    """ Class square
    """
    def __init__(self, size=0):
        """ Inizialition of variables
        Arg self identificador
        size tamañe of square
        """
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """ Inizialition of variables
        Arg self identificador
        size tamañe of square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for iterator in range(0, self.__size):
                    print("#" * self.__size)

    def area(self):
        Area = self.__size * self.__size
        return Area
