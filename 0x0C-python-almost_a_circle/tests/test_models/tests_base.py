#!/usr/bin/python3
"""Unit test for Base class"""
import unittest
from models.base import Base
import json
from models.rectangle import Rectangle
from models.square import Square
import os


class TestBaseClass(unittest.TestCase):
    """Class that holds tests for Base class"""

    def test_check_normal_id(self):
        """Check id is created and updates correctly"""
        Base. _Base__nb_objects = 0
        b = Base()
        self.assertEqual(b.id, 1)
        b = Base()
        self.assertEqual(b.id, 2)

    def test_check_passed_id(self):
        """Check to see if passing ID as a value sets correctly"""
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_check_to_json_string_method(self):
        """Check to_json_string method"""
        test = [{'id': 5}, {'height': 8}]
        testr = '[{"id": 5}, {"height": 8}]'
        self.assertEqual(Base.to_json_string(test), testr)

    def test_check_to_json_string_method_none(self):
        """Check to_json_string method when passing none"""
        test = None
        testr = '[]'
        self.assertEqual(Base.to_json_string(test), testr)

    def test_check_to_json_string_method_empty(self):
        """Check to_json_string method when passing empty list"""
        test = []
        testr = '[]'
        self.assertEqual(Base.to_json_string(test), testr)

    def test_save_to_file_method(self):
        """Check save_to_file method"""
        a = Rectangle(1, 2, 3, 4, 5)
        d = Square(1, 2, 3, 4)
        Square.save_to_file([d])
        Rectangle.save_to_file([a])
        c = [{'id': 5, 'width': 1, 'height': 2, 'x': 3, 'y': 4}]
        e = [{'id': 4, 'size': 1, 'x': 2, 'y': 3}]
        with open('Rectangle.json', encoding='utf-8') as f:
            b = json.loads(f.read())
            os.remove('./Rectangle.json')
        with open('Square.json', encoding='utf-8') as f:
            g = json.loads(f.read())
            os.remove('./Square.json')
        self.assertEqual(g, e)
        self.assertEqual(b, c)

    def test_save_to_file_method_none(self):
        """Check save_to_file method with none"""
        Rectangle.save_to_file(None)
        Square.save_to_file(None)
        c = '[]'
        with open('Rectangle.json', encoding='utf-8') as f:
            b = f.read()
            os.remove('./Rectangle.json')
        with open('Square.json', encoding='utf-8') as f:
            a = f.read()
            os.remove('./Square.json')
        self.assertEqual(b, c)
        self.assertEqual(a, c)

    def test_save_to_file_method_empty(self):
        """Check save_to_file method with empty list"""
        Rectangle.save_to_file([])
        Square.save_to_file([])
        c = '[]'
        with open('Rectangle.json', encoding='utf-8') as f:
            b = f.read()
            os.remove('./Rectangle.json')
        with open('Square.json', encoding='utf-8') as f:
            a = f.read()
            os.remove('./Square.json')
        self.assertEqual(b, c)
        self.assertEqual(a, c)

    def test_from_json_string_method(self):
        """Check from_json_string method"""
        c = [{'id': 5, 'width': 1, 'height': 2, 'x': 3, 'y': 4}]
        a = Rectangle.from_json_string('[{"height": 2, "width": 1, \
        "id": 5, "x": 3, "y": 4}]')
        self.assertEqual(a, c)

    def test_from_json_string_method_none(self):
        """Check from_json_string method with None"""
        c = []
        a = Rectangle.from_json_string(None)
        self.assertEqual(a, c)

    def test_from_json_string_method_empty(self):
        """Check from_json_string method with empty string"""
        c = []
        a = Rectangle.from_json_string('')
        self.assertEqual(a, c)

    def test_create_method(self):
        """Check create method for square and rectangle"""
        a = Rectangle(3, 5, 1, 2, 8)
        b = Square(1, 2, 3, 4)
        a = a.to_dictionary()
        b = b.to_dictionary()
        a = Rectangle.create(**a)
        b = Square.create(**b)
        self.assertEqual(a.__str__(), "[Rectangle] (8) 1/2 - 3/5")
        self.assertEqual(b.__str__(), "[Square] (4) 2/3 - 1")

    def test_load_from_file_method(self):
        """Check load_from_file method for rectangle and square"""
        a = Rectangle(1, 2, 3, 4, 5)
        b = Rectangle(5, 4, 3, 2, 1)
        d = Square(4, 3, 2, 1)
        e = Square(1, 2, 3, 4)
        Rectangle.save_to_file([a, b])
        Square.save_to_file([d, e])
        c = Rectangle.load_from_file()
        f = Square.load_from_file()
        self.assertEqual(c[0].__str__(), '[Rectangle] (5) 3/4 - 1/2')
        self.assertEqual(c[1].__str__(), '[Rectangle] (1) 3/2 - 5/4')
        self.assertEqual(f[0].__str__(), '[Square] (1) 3/2 - 4')
        self.assertEqual(f[1].__str__(), '[Square] (4) 2/3 - 1')
        os.remove('./Rectangle.json')

    def test_load_from_file_file_doesnt_exist(self):
        """Check if file doesn't exist for load_from_file"""
        self.assertEqual(Rectangle.load_from_file(), [])
        self.assertEqual(Square.load_from_file(), [])
