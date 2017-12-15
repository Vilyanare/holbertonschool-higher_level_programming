#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [[row ** 2 for row in matrix[i]]for i in range(len(matrix))]
