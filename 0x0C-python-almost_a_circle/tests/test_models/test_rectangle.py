#!/usr/bin/python3
"""Unit test for Rectangle class"""
import unittest
from models.rectangle import Rectangle
from models.base import Base
import io
import sys


class TestRectangleClass(unittest.TestCase):
    """Class that holds tests for Rectangle class"""

    def test_base_inherit(self):
        """Check rectangle inherits from Base"""
        self.assertEqual(issubclass(Rectangle, Base), True)

    def test_rectangle_id(self):
        """Check correct ID gets assigned to rectangles"""
        Base._Base__nb_objects = 0
        a = Rectangle(1, 2)
        self.assertEqual(a.id, 1)
        a = Rectangle(1, 2)
        self.assertEqual(a.id, 2)
        a = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(a.id, 5)

    def test_rectangle_no_attr(self):
        """Check rectangle when width and height aren't passed"""
        with self.assertRaises(TypeError):
            Rectangle()

    def test_rectangle_one_attr(self):
        """Check rectangle when height isn't passed"""
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_width_attribute_Rectangle(self):
        """Check width is assigned properly"""
        a = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(a.width, 1)

    def test_height_attribute_Rectangle(self):
        """Check height is assigned properly"""
        a = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(a.height, 2)

    def test_x_attribute_Rectangle(self):
        """Check x is assigned properly"""
        a = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(a.x, 3)

    def test_y_attribute_Rectangle(self):
        """Check y is assigned properly"""
        a = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(a.y, 4)

    def test_id_attribute_Rectangle(self):
        """Check id is assigned properly"""
        a = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(a.id, 5)

    def test_width_type_error_Rectangle(self):
        """Check type error for width"""
        with self.assertRaises(TypeError) as err:
            Rectangle("1", 2)
        self.assertEqual(str(err.exception), "width must be an integer")

    def test_height_type_error_rectangle(self):
        """Check type error for height"""
        with self.assertRaises(TypeError) as err:
            Rectangle(1, '2')
        self.assertEqual(str(err.exception), "height must be an integer")

    def test_x_type_error_rectangle(self):
        """Check type error for x """
        with self.assertRaises(TypeError) as err:
            Rectangle(1, 2, '3')
        self.assertEqual(str(err.exception), "x must be an integer")

    def test_y_type_error_rectangle(self):
        """Check type error for y"""
        with self.assertRaises(TypeError) as err:
            Rectangle(1, 2, 3, '4')
        self.assertEqual(str(err.exception), "y must be an integer")

    def test_width_value_error_rectangle(self):
        """Check value error for width"""
        with self.assertRaises(ValueError) as err:
            Rectangle(0, 1)
        self.assertEqual(str(err.exception), "width must be > 0")

    def test_height_value_error_rectangle(self):
        """Check value error for height"""
        with self.assertRaises(ValueError) as err:
            Rectangle(1, 0)
        self.assertEqual(str(err.exception), "height must be > 0")

    def test_x_value_error_rectangle(self):
        """Check value error for x"""
        with self.assertRaises(ValueError) as err:
            Rectangle(1, 1, -1)
        self.assertEqual(str(err.exception), "x must be >= 0")

    def test_y_value_error_rectangle(self):
        """Check value error for y"""
        with self.assertRaises(ValueError) as err:
            Rectangle(1, 1, 1, -1)
        self.assertEqual(str(err.exception), "y must be >= 0")

    def test_error_message_order_rectangle(self):
        """Check error message order (type before value)"""
        with self.assertRaises(TypeError) as err:
            Rectangle(0.0, 1)
        self.assertEqual(str(err.exception), "width must be an integer")

    def test_area_method_rectangle(self):
        """Check area method for rectangle"""
        a = Rectangle(2, 3)
        self.assertEqual(a.area(), 6)
        b = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(b.area(), 56)

    def test_display_method_rectangle(self):
        """Check display method for rectangle"""
        a = Rectangle(2, 2)
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        a.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), "##\n##\n")

    def test__str__method_rectangle(self):
        """Check __str__ method for rectangle"""
        a = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(a.__str__(), "[Rectangle] (5) 3/4 - 1/2")

    def test_display_with_xy_method_rectangle(self):
        """Check display method with x and y"""
        a = Rectangle(2, 2, 2, 2)
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        a.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), "\n\n  ##\n  ##\n")

    def test_update_method_with_args_id_rectangle(self):
        """Check update with *args (order id width height x y)"""
        a = Rectangle(1, 2, 3, 4, 5)
        a.update(10)
        self.assertEqual(a.__str__(), "[Rectangle] (10) 3/4 - 1/2")

    def test_update_method_with_args_width_rectangle(self):
        """Check update with *args (order id width height x y)"""
        a = Rectangle(1, 2, 3, 4, 5)
        a.update(10, 11)
        self.assertEqual(a.__str__(), "[Rectangle] (10) 3/4 - 11/2")

    def test_update_method_with_args_height_rectangle(self):
        """Check update with *args (order id width height x y)"""
        a = Rectangle(1, 2, 3, 4, 5)
        a.update(10, 11, 12)
        self.assertEqual(a.__str__(), "[Rectangle] (10) 3/4 - 11/12")

    def test_update_method_with_args_x_rectangle(self):
        """Check update with *args (order id width height x y)"""
        a = Rectangle(1, 2, 3, 4, 5)
        a.update(10, 11, 12, 13)
        self.assertEqual(a.__str__(), "[Rectangle] (10) 13/4 - 11/12")

    def test_update_method_with_args_y_rectangle(self):
        """Check update with *args (order id width height x y)"""
        a = Rectangle(1, 2, 3, 4, 5)
        a.update(10, 11, 12, 13, 14)
        self.assertEqual(a.__str__(), "[Rectangle] (10) 13/14 - 11/12")

    def test_update_method_with_to0_many_args_rectangle(self):
        """Check update with more than 5 *args"""
        a = Rectangle(1, 2, 3, 4, 5)
        a.update(10, 11, 12, 13, 14, 6, 7, 8)
        self.assertEqual(a.__str__(), "[Rectangle] (10) 13/14 - 11/12")

    def test_update_method_with_kwargs_rectangle(self):
        """Check update with **kwargs"""
        a = Rectangle(1, 1, 1, 1, 1)
        a.update(id=5, width=10, height=7, x=8, y=9)
        self.assertEqual(a.id, 5)
        self.assertEqual(a.width, 10)
        self.assertEqual(a.height, 7)
        self.assertEqual(a.x, 8)
        self.assertEqual(a.y, 9)

    def test_update_method_with_args_and_kwargs_rectangle(self):
        """Check update with *args and **kwargs
        (should only use *args if both are present)"""
        a = Rectangle(1, 1, 1, 1, 1)
        a.update(2, 3, 4, 5, 6, id=5, width=10, height=7, x=8, y=9)
        self.assertEqual(a.__str__(), "[Rectangle] (2) 5/6 - 3/4")

    def test_to_dictionary_rectangle(self):
        """Check to_dictionary method"""
        a = Rectangle(10, 2, 1, 9, 15)
        my_dict = {'x': 1, 'y': 9, 'id': 15, 'height': 2, 'width': 10}
        self.assertEqual(a.to_dictionary(), my_dict)
