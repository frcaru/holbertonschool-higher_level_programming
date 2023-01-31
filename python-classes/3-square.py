#!/usr/bin/python3
""" Creation of class Square defined by its size """


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

    def area(self):
        """ Returns the current square area """

        area = self.__size * self.__size
        return area
