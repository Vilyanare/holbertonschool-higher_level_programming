#!/usr/bin/python3
def uppercase(str):
    count = 0
    for c in str:
        count += 1
        if ord(c) > 96 and ord(c) < 123:
            print("{:c}".format(ord(c) - 32), end='')
        else:
            print("{:c}".format(ord(c)), end="")
        if count == len(str):
            print("")
