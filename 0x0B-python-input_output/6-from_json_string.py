#!/usr/bin/python3
def from_json_string(my_str):
    """returns a python object from a JSON string"""
    import json
    return json.JSONDecoder().decode(my_str)
