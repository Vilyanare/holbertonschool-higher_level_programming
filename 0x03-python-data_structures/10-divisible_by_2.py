#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    bool_list = []
    for i in range(len(my_list)):
        bool_list.append(not(my_list[i] % 2))
    return bool_list
