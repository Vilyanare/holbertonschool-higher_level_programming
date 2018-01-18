#!/usr/bin/python3
def load_from_json_file(filename):
    """Reads JSON string from file and decodes it into a python object"""
    import json
    with open(filename, 'r', encoding="utf-8") as a_file:
        return json.load(a_file)
