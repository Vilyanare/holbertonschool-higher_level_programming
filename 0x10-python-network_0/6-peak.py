#!/usr/bin/python3
'''
holds the function find_peak
'''


def find_peak(list_of_integers):
    '''
    finds a peak number in a list of integers
    '''
    new_list = list_of_integers[:1]
    for x in range(1, len(list_of_integers)):
        if list_of_integers[x] != list_of_integers[x - 1]:
            new_list.append(list_of_integers[x])

    while new_list:
        half = int(len(new_list) / 2)
        pivot = new_list[half]
        if half - 1 < 0:
            lower = 0
        else:
            lower = new_list[half - 1]
        if half + 1 > len(new_list) - 1:
            upper = 0
        else:
            upper = new_list[half + 1]
        if lower < pivot > upper:
            return pivot
        if upper > pivot:
            new_list = new_list[half - 1:]
        else:
            new_list = new_list[:half]
