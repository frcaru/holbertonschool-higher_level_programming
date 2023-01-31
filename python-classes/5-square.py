#!/usr/bin/python3
""" Creation of class Square defined by its size """


class Square:
    """ Class Square

    Attribute:
    __size : the size of the square

    Method:
    area() : returns the square area

    """

    def __init__(self, __size=0):
        """ Constructor method """

        if isinstance(__size, int) is not True:
            raise TypeError("size must be an integer")
        if __size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = __size

    def area(self):
        """ Method that returns the current square area """

        return (self.__size) ** 2

    @property
    def size(self):
        """ Getter method """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter method """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """ Method that prints the square with the # char """

        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("")
