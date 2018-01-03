#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        x = sum([i[0] * i[1] for i in my_list])
        y = sum([i[1] for i in my_list])
        return x / y
    else:
        return 0
