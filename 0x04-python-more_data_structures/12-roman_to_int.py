#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is str and roman_string:
        number = 0
        s = roman_string
        rom = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
        for i in roman_string:
            x = roman_string.index(i)
            if x < len(s) - 1:
                number += rom[i] if rom[i] >= rom[s[x + 1]] else rom[i] * -1
            else:
                number += rom[i]
        return number
    else:
        return 0
