#!/usr/bin/python3


def no_c(my_string):

    copy = ""
    for i in my_string:
        if i == 'c' or i == 'C':
            copy += ''
        else:
            copy += i

    return copy
