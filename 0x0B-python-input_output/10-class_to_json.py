#!/usr/bin/python3
def class_to_json(obj):
    """Returns dictionary description of attributes in a class"""
    return obj.__dict__
