#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Class that holds all test functions"""

    def test_find_max(self):
        """Test standard input/output"""
        self.assertEqual(max_integer([1, 2, 4, 3]), 4)

    def test_type(self):
        """Tests list variable for type"""
        with self.assertRaises(TypeError):
            max_integer("test")

    def test_empty(self):
        """Checks return on empty list"""
        self.assertEqual(max_integer([]), None)

    def test_negative(self):
        """Checks list with negative number in it"""
        self.assertEqual(max_integer([-1, 3, 4]), 4)

    def test_all_negative(self):
        """Check a list with all negative numbers"""
        self.assertEqual(max_integer([-3, -2, -1]), -1)

    def test_wrong_type_in_list(self):
        """Check if list contains non integer"""
        with self.assertRaises(TypeError):
            max_integer([1, "hello", 2, 3])
