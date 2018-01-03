#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is str and roman_string:
        number = 0
        s = roman_string
        rom = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
        for i in range(len(roman_string)):
            if i < len(s) - 1:
                number += rom[s[i]] if rom[s[i]] >= rom[s[i + 1]] else rom[s[i]] * -1
            else:
                number += rom[s[i]]
        return number
    else:
        return 0
