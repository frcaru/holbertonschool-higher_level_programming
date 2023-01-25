#!/usr/bin/python3


def check_tuple(tuple_x=()):

    list_x = list(tuple_x)

    if len(list_x) < 1:
        list_x = (0, 0)
    elif len(list_x) < 2:
        list_x.append(0)
    tuple_x = tuple(list_x)
    return tuple_x


def add_tuple(tuple_a=(), tuple_b=()):

    tuple_a = check_tuple(tuple_a)
    tuple_b = check_tuple(tuple_b)

    new_tuple = ((tuple_a[0] + tuple_b[0]), (tuple_a[1] + tuple_b[1]))
    return new_tuple
