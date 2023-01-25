#!/usr/bin/python3


def multiple_returns(sentence):

    if not sentence:
        sentence.append(None)
    new_tuple = (len(sentence), sentence[0])
    return new_tuple
