#!/usr/bin/python3
""" Function that removes all
    characters c and C from a string.
"""


def no_c(my_string):
    new_string = []
    for i in range(len(my_string)):
        if my_string[i] != 'C' and my_string[i] != 'c':
            new_string.append(my_string[i])
    return ("".join(map(str, new_string)))

# def no_c2(my_string):
#     new_string = []
#     for letter in my_string:
#         if letter != 'C' and letter != 'c':
#             new_string.append(letter)
#     return ("".join(map(str, new_string)))
