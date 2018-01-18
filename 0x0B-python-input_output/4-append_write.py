#!/usr/bin/python3
def append_write(filename="", text=""):
    """Appends text to a file and returns how many characters were written"""
    first = 0
    second = 0
    try:
        with open(filename, mode="r", encoding='utf-8') as a_file:
            first = len(a_file.read())
    except:
        pass
    with open(filename, mode='a+', encoding='utf-8') as a_file:
        a_file.write(text)
    with open(filename, encoding='utf-8') as a_file:
        second = len(a_file.read())
    return second - first
