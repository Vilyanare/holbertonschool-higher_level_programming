#!/usr/bin/python3
def uppercase(str):
    count = 0
    for c in str:
        a = ord(c)
        count += 1
        if ord(c) > 96 and ord(c) < 123:
            a -= 32
        print("{:c}".format(a), end='')
        if count == len(str):
            print("")
