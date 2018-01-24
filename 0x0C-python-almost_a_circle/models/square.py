#!/usr/bin/python3
"""Module containing the Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class for defining and working with squares"""

    def __init__(self, size, x=0, y=0, id=None):
        """
        instantiates class Square

        Attributes
        @size: length of one side of the square
        @x: How many collumsn in to start printing
        @y: How many rows in to start printing
        @id: Unique id of instance
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return an informal represenation of Square"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """Assigns argument to each attribute
        Uses keyword assignment unless there are arguments in *args"""
        if args:
            attrs = ['id', 'size', 'x', 'y']
            for (a, v) in zip(attrs, args):
                setattr(self, a, v)
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """returns a dictionary definition of a Rectangle
        Including attributes
        id
        size
        x
        y
        """
        rep = {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
        return rep

    @property
    def size(self):
        """getter for size attribute"""
        return self.height

    @size.setter
    def size(self, value):
        """setter for size attribute"""
        self.width = value
        self.height = value
