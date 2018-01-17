#!/usr/bin/python3
def is_same_class(obj, a_class):
    """Checks to see if the object is exactly from a_class"""
    return True if type(obj) == a_class else False
