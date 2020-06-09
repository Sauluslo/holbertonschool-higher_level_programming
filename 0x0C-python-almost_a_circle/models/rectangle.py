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
