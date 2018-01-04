#!/usr/bin/python3
class Square:

    def __init__(self, size=0):
        """Initializes size attribute with type protection
        and can't be less than 0"""

        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """Returns size of Square"""

        return self.__size

    @size.setter
    def size(self, value):
        """Sets size of Square"""

        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns area of Square"""

        return self.__size * self.__size
