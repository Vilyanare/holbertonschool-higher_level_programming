#!/usr/bin/python3
"""
Module defining class Rectangle
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry
class Rectangle(BaseGeometry):
    """defining Rectangle class"""
    def __init__(self, width, height):
        """Initializes an instance of the Rectangle class"""
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns area of a Rectangle instance"""
        return self.__width * self.__height

    def __str__(self):
        """Returns an informal definition of the Rectangle class"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
