#!/usr/bin/python3
def read_file(filename=""):
    """Method for reading and printing a file to stdout"""
    with open(filename, encoding='utf-8') as a_file:
        print(a_file.read(), end="")
