#!/usr/bin/python3
"""Stand alone function that divides all elements of a matrix
by n"""


def matrix_divided(matrix, div):
    """Function that divides a matrix by div"""
    length = 0
    new_matrix = []
    if type(matrix) != list:
        raise TypeError('matrix must be a matrix \
(list of lists) of integers/floats')
    try:
        for i in range(len(matrix)):
            if type(matrix[i]) != list:
                raise TypeError('matrix must be a matrix \
(list of lists) of integers/floats')
            length = len(matrix[0])
            if len(matrix[i]) != length:
                raise TypeError('Each row of the matrix \
must have the same size')
            new_matrix.append([])
            for x in range(len(matrix[i])):
                if type(matrix[i][x]) not in (int, float):
                    raise TypeError('matrix must be a matrix \
(list of lists) of integers/floats')
                if type(div) not in (int, float):
                    raise TypeError('div must be a number')
                if div == 0:
                    raise ZeroDivisionError('division by zero')
                new_matrix[i].append(round(matrix[i][x] / div, 2))
    except:
        raise
    return new_matrix
