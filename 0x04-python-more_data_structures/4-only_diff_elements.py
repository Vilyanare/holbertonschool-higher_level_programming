#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new = list(set_1) + list(set_2)
    return [i for i in new if i not in set_1 or i not in set_2]
