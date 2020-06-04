#!/usr/bin/python3
""" 13-student.py
"""


class Student:
    """ Class Student that defines a student by: (based on 12-student.py)
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        my_dict = {}
        for Elements in attrs:
            if hasattr(self, Elements):
                my_dict[Elements] = getattr(self, Elements)
        return my_dict

    def reload_from_json(self, json):
        for Elements in json:
            self.__dict__[Elements] = json[Elements]
