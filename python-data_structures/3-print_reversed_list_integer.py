#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):

    if not my_list:
        return None
    i = len(my_list)
    count = 0
    while count <= len(my_list):
        if i == 0:
            break
        else:
            print("{:d}".format(my_list[i - 1]))
            i -= 1
            count += 1
