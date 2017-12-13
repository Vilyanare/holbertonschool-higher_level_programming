#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list_a = []
    list_b = []
    for x in range(2):
        try:
            list_a.append(tuple_a[x])
        except IndexError:
            list_a.append(0)
        try:
            list_b.append(tuple_b[x])
        except IndexError:
            list_b.append(0)
    tuple_a = tuple(list_a)
    tuple_b = tuple(list_b)
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
