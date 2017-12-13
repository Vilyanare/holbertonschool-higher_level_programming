#!/usr/bin/python3
def no_c(my_string):
    count = 0
    for i in my_string:
        if i == "c" or i == "C":
            my_string = my_string[:count] + my_string[count + 1:]
            count -= 1
        count += 1
    return my_string
