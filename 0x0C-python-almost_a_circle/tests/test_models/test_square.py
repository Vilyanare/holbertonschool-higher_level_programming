#!/usr/bin/python3
"""Unit test for Square class"""
import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base
import io
import sys


class TestSquareClass(unittest.TestCase):
    """Class that holds tests for Square class"""

    def test_rectangle_inherit(self):
        """Check Square inherits from Base"""
        self.assertEqual(issubclass(Square, Rectangle), True)

    def test_square_id(self):
        """Check correct ID gets assigned to square"""
        Base._Base__nb_objects = 0
        a = Square(1)
        self.assertEqual(a.id, 1)
        a = Square(1)
        self.assertEqual(a.id, 2)
        a = Square(1, 2, 3, 4)
        self.assertEqual(a.id, 4)

    def test_square_no_attr(self):
        """Check square when size isn't passed"""
        with self.assertRaises(TypeError):
            Square()

    def test_size_attribute_Square(self):
        """Check size is assigned properly"""
        a = Square(1, 2, 3, 4)
        self.assertEqual(a.size, 1)

    def test_x_attribute_Square(self):
        """Check x is assigned properly"""
        a = Square(1, 2, 3, 4)
        self.assertEqual(a.x, 2)

    def test_y_attribute_Square(self):
        """Check y is assigned properly"""
        a = Square(1, 2, 3, 4)
        self.assertEqual(a.y, 3)

    def test_id_attribute_Square(self):
        """Check id is assigned properly"""
        a = Square(1, 2, 3, 4)
        self.assertEqual(a.id, 4)

    def test_size_type_error(self):
        """Check type error for size"""
        with self.assertRaises(TypeError):
            Square("1")

    def test_x_type_error(self):
        """Check type error for x """
        with self.assertRaises(TypeError):
            Square(1, '2')

    def test_y_type_error(self):
        """Check type error for y"""
        with self.assertRaises(TypeError):
            Square(1, 2, '3')

    def test_size_value_error(self):
        """Check value error for size"""
        with self.assertRaises(ValueError):
            Square(0)

    def test_x_value_error(self):
        """Check value error for x"""
        with self.assertRaises(ValueError):
            Square(1, -1)

    def test_y_value_error(self):
        """Check value error for y"""
        with self.assertRaises(ValueError):
            Square(1, 1, -1)

    def test_error_message_order(self):
        """Check error message order (type before value)"""
        with self.assertRaises(TypeError):
            Square(0.0)

    def test_area_method(self):
        """Check area method for Square"""
        a = Square(2)
        self.assertEqual(a.area(), 4)
        b = Square(8, 0, 0, 12)
        self.assertEqual(b.area(), 64)

    def test_display_method(self):
        """Check display method for Square"""
        a = Square(2)
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        a.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), "##\n##\n")

    def test__str__method(self):
        """Check __str__ method for Square"""
        a = Square(1, 2, 3, 4)
        self.assertEqual(a.__str__(), "[Square] (4) 2/3 - 1")

    def test_display_with_xy_method(self):
        """Check display method with x and y"""
        a = Square(2, 2, 2, 2)
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        a.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), "\n\n  ##\n  ##\n")

    def test_update_method_with_args_id(self):
        """Check update with *args (order id width height x y)"""
        a = Square(1, 2, 3, 4)
        a.update(10)
        self.assertEqual(a.__str__(), "[Square] (10) 2/3 - 1")

    def test_update_method_with_args_size(self):
        """Check update with *args (order id width height x y)"""
        a = Square(1, 2, 3, 4)
        a.update(10, 11)
        self.assertEqual(a.__str__(), "[Square] (10) 2/3 - 11")

    def test_update_method_with_args_x(self):
        """Check update with *args (order id width height x y)"""
        a = Square(1, 2, 3, 4)
        a.update(10, 11, 12)
        self.assertEqual(a.__str__(), "[Square] (10) 12/3 - 11")

    def test_update_method_with_args_y(self):
        """Check update with *args (order id width height x y)"""
        a = Square(1, 2, 3, 4)
        a.update(10, 11, 12, 13)
        self.assertEqual(a.__str__(), "[Square] (10) 12/13 - 11")

    def test_update_method_with_too_many_args_square(self):
        """Check update with more than 4 *args"""
        a = Square(1, 2, 3, 4)
        a.update(10, 11, 12, 13, 4, 2, 5, 1, 2)
        self.assertEqual(a.__str__(), "[Square] (10) 12/13 - 11")

    def test_update_method_with_kwargs(self):
        """Check update with **kwargs"""
        a = Square(1, 1, 1, 1)
        a.update(id=5, size=4, x=8, y=9)
        self.assertEqual(a.id, 5)
        self.assertEqual(a.size, 4)
        self.assertEqual(a.x, 8)
        self.assertEqual(a.y, 9)

    def test_update_method_with_args_and_kwargs(self):
        """Check update with *args and **kwargs
        (should only use *args if both are present)"""
        a = Square(1, 1, 1, 1)
        a.update(2, 3, 4, 5, id=5, size=10, x=8, y=9)
        self.assertEqual(a.__str__(), "[Square] (2) 4/5 - 3")

    def test_to_dictionary_square(self):
        """Check to_dictionary method"""
        a = Square(10, 1, 9, 15)
        my_dict = {'x': 1, 'y': 9, 'id': 15, 'size': 10}
        self.assertEqual(a.to_dictionary(), my_dict)
