#!/usr/bin/python3
"""Module that contains Student class"""


class Student:
    """Defines the Student class"""

    def __init__(self, first_name, last_name, age):
        """Initialization of Student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns dictionary representation of attributes"""
        return self.__dict__
