#!/usr/bin/python3
def save_to_json_file(my_obj, filename):
    """Save a python object to a file as a JSON string representation"""
    import json
    with open(filename, "w+", encoding="utf-8") as a_file:
        json.dump(my_obj, a_file)
