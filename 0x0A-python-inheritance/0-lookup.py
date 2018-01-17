#!/usr/bin/python3
def lookup(obj):
    """Returns attributes and methods of a given object"""
    return list(dir(obj))
