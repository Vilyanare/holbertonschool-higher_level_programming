#!/usr/bin/python3
"""Module holding the class MyInt"""


class MyInt(int):
    """MyInt class reversing == and != operators"""
    def __eq__(self, a):
        """Reverse EQ with NE method"""
        return int.__ne__(self, a)

    def __ne__(self, a):
        """Reverse NE with EQ method"""
        return int.__eq__(self, a)
