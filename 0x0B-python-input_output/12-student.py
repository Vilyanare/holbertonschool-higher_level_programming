#!/usr/bin/python3
"""Module that contains Student class"""


class Student:
    """Defines the Student class"""

    def __init__(self, first_name, last_name, age):
        """Initialization of Student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns dictionary representation of attributes
        if attrs is not none only return keys from attrs
        """
        temp = {}
        if attrs is not None:
            for k, v in self.__dict__.items():
                if k in attrs:
                    temp[k] = v
            return temp
        return self.__dict__
