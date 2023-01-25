#!/usr/bin/python3


def multiple_returns(sentence):

    print(len(sentence))
    if len(sentence) < 1:
        new_tuple = (len(sentence), None)
    else:
        new_tuple = (len(sentence), sentence[0])
    return new_tuple
