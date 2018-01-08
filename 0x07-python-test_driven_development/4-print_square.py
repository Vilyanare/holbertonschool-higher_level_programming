#!/usr/bin/python3
""""Single function module"""


def print_square(size):
    """print a square of # of size n"""
    if type(size) != int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if size == 0:
        print()
    for i in range(size):
        for x in range(size):
            print("#", end="")
        print()
