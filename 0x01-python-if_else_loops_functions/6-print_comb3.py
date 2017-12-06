#!/usr/bin/python3
for i in range(0, 10):
    for x in range(0, 10):
        if i < x and i != x:
            if i != 0 or x != 1:
                print(", ", end="")
            print("{}{}".format(chr(i + 48), chr(x + 48)), end='')
        if i == 9 and x == 9:
            print("")
