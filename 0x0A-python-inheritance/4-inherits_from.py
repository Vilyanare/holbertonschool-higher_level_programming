#!/usr/bin/python3
def inherits_from(obj, a_class):
    """Checks if an object is inherited from a_class"""
    if type(obj) != a_class and isinstance(obj, a_class):
        return True
    else:
        return False
