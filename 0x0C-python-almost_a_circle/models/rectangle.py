#!/usr/bin/python3
"""Module holding the Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Class for defining and working with rectangles"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Instantiating method for Rectangle class

        Attributes
        @size: length of one side of the square
        @x: How many collumsn in to start printing
        @y: How many rows in to start printing
        @id: Unique id of instance
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        """Return an informal description of Rectangle class"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
        self.id, self.x, self.y, self.width, self.height)

    def area(self):
        """Returns area of Rectangle"""
        return self.width * self.height

    def display(self):
        """Prints a text representation of the Rectangle with # char.
        Print starts printing at x/y position"""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            for _ in range(self.x):
                print(" ", end="")
            for _ in range(self.width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """Assigns argument to each attribute
        Uses keyword assignment unless there are arguments in *args"""
        if args:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for (a, v) in zip(attrs, args):
                setattr(self, a, v)
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """returns a dictionary definition of a Rectangle
        Including attributes
        id
        width
        height
        x
        y
        """
        rep = {'id': self.id, 'width': self.width,
         'height': self.height, 'x': self.x, 'y': self.y}
        return rep

    @property
    def height(self):
        """Getter for height for attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height for attribute"""
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def width(self):
        """Getter for width for attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width for attribute"""
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def x(self):
        """Getter for x for attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x for attribute"""
        if type(value) != int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= to 0')
        self.__x = value

    @property
    def y(self):
        """Getter for y for attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y for attribute"""
        if type(value) != int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= to 0')
        self.__y = value
