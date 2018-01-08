#!/usr/bin/python3
"""0-add_integer module

Has one function, add_integer(a, b)"""


def add_integer(a, b):
    """
        Returns the sum of two integers or floats cast to int
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
