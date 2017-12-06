#!/usr/bin/python3
def uppercase(str):
    for c in str:
        a = ord(c)
        if ord(c) > 96 and ord(c) < 123:
            a -= 32
        print("{:c}".format(a), end='')
    print("")
