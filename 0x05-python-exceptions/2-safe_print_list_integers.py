#!/usr/bin/python3
def safe_print_list_integers(my_lists=[], x=0):
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_lists[i]), end="")
            count += 1
        except (ValueError):
            pass
    print()
    return count
