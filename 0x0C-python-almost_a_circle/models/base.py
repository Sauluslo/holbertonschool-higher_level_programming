#!/usr/bin/python3
""" Class Base
"""
import json


class Base:
    """ Declare Attribute of the class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Init of the id
            in the class base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
