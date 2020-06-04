#!/usr/bin/python3
""" 5-to_json_string.py
"""
import json


def save_to_json_file(my_obj, filename):
    """ function that returns an object
        (Python data structure) represented
        by a JSON string:
    """
    with open(filename, 'w', encoding="utf-8") as file:
        file.write(json.dumps(my_obj))
