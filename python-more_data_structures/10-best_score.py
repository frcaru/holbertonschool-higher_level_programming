#!/usr/bin/python3


def best_score(a_dictionary):

    bestkey =""
    max = 0

    if not a_dictionary:
        return None
    for key in a_dictionary:
        if max < a_dictionary[key]:
            bestkey = key
            max = a_dictionary[key]
    return bestkey
