#!/usr/bin/python3


def roman_to_int(roman_string):

    if not roman_string:
        return None
    result = 0

    for r in roman_string:
        if r == 'M':
            if roman_string[roman_string.index(r) - 1] == 'C':
                result += 900
            else:
                result += 1000

        if r == 'D':
            if roman_string[roman_string.index(r) - 1] == 'C':
                result += 400
            else:
                result += 500

        if r == 'C':
            if roman_string[roman_string.index(r) - 1] == 'X':
                result += 90
            else:
                result += 100

        if r == 'L':
            if roman_string[roman_string.index(r) - 1] == 'X':
                result += 40
            else:
                result += 50

        if r == 'X':
            if roman_string[roman_string.index(r) - 1] == 'I':
                result += 9
            else:
                result += 10

        if r == 'V':
            if roman_string[roman_string.index(r)] == roman_string[0]:
                result += 5
            elif roman_string[roman_string.index(r) - 1] == 'I':
                result += 4
            else:
                result += 5

        if r == 'I':
            if roman_string[roman_string.index(r) + 1] == 'I':
                result += 1

    return result
