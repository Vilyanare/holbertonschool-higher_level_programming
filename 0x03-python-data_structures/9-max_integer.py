#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list):
        for i in range(len(my_list) - 1):
            if my_list[i] > my_list[i + 1]:
                temp = my_list[i]
                my_list[i] = my_list[i + 1]
                my_list[i + 1] = temp
        return my_list[len(my_list) - 1]
    return "None"
