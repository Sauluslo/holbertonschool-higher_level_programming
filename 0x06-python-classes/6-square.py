#!/usr/bin/python3
"6-square.py define"


class Square:
    """ Class square
    """
    def __init__(self, size=0, position=(0, 0)):
        """ Inizialition of variables
        Arg self identificador
        size tamañe of square
        """
        self.size = size
        self.position = position

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
        """Inizialitation of variables
        Arg self identificador
        """
        if self.__size == 0:
            print()
        else:
            for row in range(self.__position[1]):
                print()
            for row in range(0, self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def area(self):
        Area = self.__size * self.__size
        return Area
