#!/usr/bin/python3
"""Module containing Rectangle class"""


class Rectangle:
    """Class for defining and returning dimensions of a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializing method"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width attribute"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Getter for height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height attribute"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Method for getting area of a rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Method for getting perimiter of a rectangle"""
        if self.height == 0 or self.width == 0:
            return 0
        else:
            return (self.width * 2) + (self.height * 2)
