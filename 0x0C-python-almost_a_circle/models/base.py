#!/usr/bin/python3
"""Module holding the Base class"""
import json
import turtle


class Base:
    """
    Assigns unique ID to each instance

    Attributes
    @__n_objects: Keeps track of how many instances are created
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiation method for Base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws squares and rectangles with turtle module"""
        turtle.hideturtle()
        turtle.speed(0)
        new = list_rectangles + list_squares
        for i in new:
            turtle.up()
            turtle.goto(i.x, i.y)
            turtle.pd()
            turtle.forward(i.width)
            turtle.left(90)
            turtle.forward(i.height)
            turtle.left(90)
            turtle.forward(i.width)
            turtle.left(90)
            turtle.forward(i.height)
            turtle.left(90)

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
        info = '[]'
        if list_objs:
            info = Base.to_json_string(
                [cls.to_dictionary(v) for v in list_objs])
        with open("{}.json".format(
                cls.__name__), 'w', encoding="utf-8") as f:
            f.write(info)

    @staticmethod
    def from_json_string(json_string):
        """Returns a list of dictionaries and takes a
        json encoded list of dictionary strings"""
        new = []
        if json_string:
            new = json.loads(json_string)
        return new

    @classmethod
    def create(cls, **dictionary):
        """returns an instance of a sub class with attributes set to
        passed values"""
        if "size" in dictionary:
            temp = cls(1)
        else:
            temp = cls(1, 1)
        temp.update(**dictionary)
        return temp

    @classmethod
    def load_from_file(cls):
        """Creates instances of sub classes of Base from a
        json encoded string held in a file"""
        try:
            with open("{}.json".format(cls.__name__), encoding='utf-8') as f:
                return [cls.create(
                    **i) for i in Base.from_json_string(f.read())]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Turns a list of rectangles or squares into a CSV file"""
        comma = False
        attrs = ['id', 'size', 'x', 'y']
        if cls.__name__ == 'Rectangle':
            attrs = ['id', 'width', 'height', 'x', 'y']
        with open("{}.csv".format(cls.__name__), "w", encoding='utf-8') as f:
            for i in list_objs:
                for x in attrs:
                    if comma is True:
                        f.write(",")
                    comma = True
                    f.write("{}".format(eval("i.{}".format(x))))

    @classmethod
    def load_from_file_csv(cls):
        """Creates a rectangle or square from a CSV file"""
        ret = []
        hold = {}
        attrs = ['id', 'size', 'x', 'y']
        count = 4
        if cls.__name__ == 'Rectangle':
            attrs = ['id', 'width', 'height', 'x', 'y']
            count = 5
        with open('{}.csv'.format(cls.__name__), encoding='utf-8') as f:
            val = f.read()
        val = val.split(',')
        val = [int(i) for i in val]
        while val:
            for n, v in enumerate(attrs):
                hold[v] = val[n]
            val = val[count:]
            ret.append(cls.create(**hold))
        return ret
