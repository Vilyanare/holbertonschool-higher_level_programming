#!/usr/bin/python3
class Square:

    def __init__(self, size=0, position=(0, 0)):
        """Initializes square class
        Attributes:
            @size: length of one side of the square
            @position: where to start printing square"""

        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Returns position of Square"""

        return self.__position

    @position.setter
    def position(self, value):
        """Sets position of Square"""
        a = value
        if type(a) != tuple or len(a) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(a[0]) != int or type(a[1]) != int or a[0] < 0 or a[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Returns area of Square"""

        return self.__size * self.__size

    def my_print(self):
        """Print the square to stdout with #
        Pad with spaces and newlines by position"""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            for _ in range(self.__position[0]):
                print(" ", end="")
            for _ in range(self.__size):
                print("#", end="")
            print()
