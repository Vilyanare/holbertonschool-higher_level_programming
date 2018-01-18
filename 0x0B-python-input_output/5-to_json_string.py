#!/usr/bin/python3
def to_json_string(my_obj):
    """Return a JSON representation of an object"""
    import json
    return json.JSONEncoder().encode(my_obj)
