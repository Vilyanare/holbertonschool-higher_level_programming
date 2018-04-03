#!/usr/bin/env python3
'''
holds the function find_peak
'''


def find_peak(list_of_integers):
    '''
    finds a peak number in a list of integers
    '''
    new_list = list_of_integers
    while True:
        half = len(new_list) / 2
        pivot = new_list[half]
        if new_list[half - 1] < pivot > new_list[half + 1]:
            return pivot
        if new_list[half + 1] > pivot:
            new_list = new_list[half - 1:]
        else:
            new_list = new_list[:half]
