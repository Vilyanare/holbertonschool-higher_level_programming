#!/usr/bin/python3
odd = 0
for i in range(122, 96, -1):
    odd += 1
    c = i
    if odd % 2 == 0:
        c -= 32
    print("{:c}".format(c), end='')
