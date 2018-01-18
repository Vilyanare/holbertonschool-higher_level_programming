#!/usr/bin/python3
def write_file(filename="", text=""):
    """method to write text to a file and return characters written"""
    with open(filename, mode='w', encoding='utf-8') as a_file:
        a_file.write(text)
    with open(filename, encoding='utf-8') as a_file:
        return len(a_file.read())
