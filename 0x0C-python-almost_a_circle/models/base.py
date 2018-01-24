#!/usr/bin/python3
"""Module holding the Base class"""
import json


class Base:
    """
    Assigns unique ID to each instance

    Attributes
    @__n_objects: Keeps track of how many instances are created
    """
    __nb_objects=0

    def __init__(self, id=None):
        """Instantiation method for Base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns a json representation of the input dictionary"""
        new = '[]'
        if list_dictionaries is not None:
            new = json.dumps(list_dictionaries)
        return new

    @classmethod
    def save_to_file(cls, list_objs):
        """save json representation of a class to a file"""
        info = Base.to_json_string([cls.to_dictionary(v) for v in list_objs])
        with open("{}.json".format(cls.__name__), 'w',
        encoding="utf-8") as f:
            f.write(info)

    @staticmethod
    def from_json_string(json_string):
        """Returns a list of dictionaries and takes a
        json encoded list of dictionary strings"""
        new = []
        if json_string is not None:
            new = json.loads(json_string)
        return new

    @classmethod
    def create(cls, **dictionary):
        """returns an instance of a sub class with attributes set to
        passed values"""
        temp = cls(1,1)
        temp.update(**dictionary)
        return temp

    @classmethod
    def load_from_file(cls):
        """Creates instances of sub classes of Base from a
        json encoded string held in a file"""
        try:
            with open("{}.json".format(cls.__name__), encoding='utf-8') as f:
                return [cls.create(**i) for i in Base.from_json_string(f.read())]
        except FileNotFoundError:
            return []
