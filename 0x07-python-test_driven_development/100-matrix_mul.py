#!/usr/bin/python3
"""Single function module"""


def matrix_mul(m_a, m_b):
    """Function that multiplies two matrices together"""
    new_matrix = []
    if type(m_a) != list:
        raise TypeError('m_a must be a list')
    if type(m_b) != list:
        raise TypeError('m_b must be a list')
    if len(m_a) == 0:
        raise  ValueError("m_a can't be empty")
    if len(m_b) == 0:
        raise  ValueError("m_b can't be empty")
    for i in m_a:
        if not isinstance(i, list):
            raise TypeError('m_a must be a list')
    for i in m_b:
        if not isinstance(i, list):
            raise TypeError('m_b must be a list')
    m_a_len = len(m_a[0])
    m_b_len = len(m_a[0])
    new = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    for row in range(len(m_a)):
        if len(m_a[row]) != m_a_len:
            raise TypeError('each row of m_a must should be of the same size')
        for col in range(len(m_a[0])):
            if len(m_b[col]) != m_b_len:
                raise TypeError('each row of m_b must should be of the same size')
            for col_b in range(len(m_b[0])):
                if not isinstance(m_a[row][col], (int, float)):
                    raise TypeError('m_a should contain only integers or floats')
                if not isinstance(m_b[col][col_b], (int, float)):
                    raise TypeError('m_b should contain only integers or floats')
                new[row][col_b] += m_a[row][col] * m_b[col][col_b]
    return new
