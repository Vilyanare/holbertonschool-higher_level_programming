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

    def area(self):
        """Returns area of Square"""

        return self.__size * self.__size
