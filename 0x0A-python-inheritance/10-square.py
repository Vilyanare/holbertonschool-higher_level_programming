#!/usr/bin/python3
"""
Module defines a Square class
"""
Rectangle = __import__("9-rectangle").Rectangle
class Square(Rectangle):
    """Defining the class Square"""
    def __init__(self, size):
        """Initializing an instance of the class Square"""
        Rectangle.__init__(self, size, size)
        self.integer_validator("size", size)
        self.__size = size
