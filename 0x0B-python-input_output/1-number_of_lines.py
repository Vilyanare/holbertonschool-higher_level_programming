#!/usr/bin/python3
def number_of_lines(filename=""):
    """returns number of lines in a file"""
    with open(filename, encoding='utf-8') as a_file:
        count = 0
        for lines in a_file:
            count += 1
        return count
