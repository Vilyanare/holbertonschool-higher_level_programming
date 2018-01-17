#!/usr/bin/python3
"""Method with an empty class"""


class BaseGeometry:
    """Empty class"""

    def area(self):
        """Holds temp message for method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value attribute"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
