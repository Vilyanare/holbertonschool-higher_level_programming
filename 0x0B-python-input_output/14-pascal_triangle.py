#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return []
    tripiece = [1]
    triangle = []
    triangle.append(tripiece)
    for x in range(1, n):
        count = 1
        newtripiece = []
        for i in range(x + 1):
            if i == 0 or i == len(tripiece):
                newtripiece.append(1)
            elif i <= len(tripiece) / 2:
                newtripiece.append(tripiece[i] + tripiece[i - 1])
            else:
                if len(tripiece) % 2 == 0 and count == 1:
                    count += 1
                newtripiece.append(newtripiece[i - count])
                count += 2
        tripiece = newtripiece[:]
        triangle.append(tripiece)
    return triangle
