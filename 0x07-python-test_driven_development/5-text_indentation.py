#!/usr/bin/python3
"""Single function module"""


def text_indentation(text):
    """Function that prints given text with 2 new lines after
    specific characters (. ? :)"""
    if type(text) != str:
        raise TypeError('text must be a string')
    last = ""
    f = 0
    for i in text:
        if i in ('.', '?', ':'):
            print("{}\n".format(i))
            f = 1
        elif f == 1:
            if i != ' ':
                f = 0
                print("{}".format(i), end="")
        else:
            print("{}".format(i), end="")
        last = i
    if last not in ('.', '?', ':'):
        print()
