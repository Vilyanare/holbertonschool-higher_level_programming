#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    """method to read n lines of a file"""
    with open(filename, encoding='utf-8') as a_file:
        count = 0
        for num, line in enumerate(a_file, 1):
            print(line, end="")
            if num == nb_lines:
                break
