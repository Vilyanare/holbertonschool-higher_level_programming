#!/usr/bin/python3
"""Module holding a sub class of list"""
class MyList(list):
    """Sub class of list class"""
    def print_sorted(self):
        """Method to print a sorted version of your list"""
        new = self[:]
        new.sort()
        print(new)
