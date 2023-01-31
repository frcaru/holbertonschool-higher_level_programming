#!/usr/bin/python3
""" Creation of a class named Square that's defined by
private attribute __size """


class Square:
    """ Class Square

    Private attribute:
    __size : the size of the square
    """

    def __init__(self, __size=0):

        if isinstance(__size, int) is not True:
            raise TypeError("size must be an integer")

        if __size < 0:
            raise ValueError("size must be >= 0")

        else:
            self.__size = __size
