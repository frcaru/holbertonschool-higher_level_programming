#!/usr/bin/python3


def roman_to_int(roman_string):

#M = 1000
#D = 500
#C = 100
#L = 50
#X = 10
#V = 5
#I = 1

    roman_dict = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1,
    }

    if not isinstance(roman_string, str) or roman_string == None:
        return 0

    summ = 0

    for i in range(len(roman_string) - 1, -1, -1):
        num = roman_dict[roman_string[i]]
        if 3 * num < summ:
            summ -= num
        else:
            summ += num
    return summ
