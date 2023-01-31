#!/usr/bin/python3
""" Creation of class Square defined by its size """


class Square:
    """ Class Square

    Attribute:
    __size : the size of the square
    __position : a tuple of 2 positive integers

    Method:
    area() : returns the square area
    my_print() : prints the square with # characters


    """

    def __init__(self, __size=0, __position=(0, 0)):
        """ Constructor method """

        self.__size = __size
        self.__position = __position

    def area(self):
        """ Method that returns the current square area """

        return (self.__size) ** 2

    @property
    def position(self):
        """ Getter method """
        return self.__position

    @position.setter
    def position(self, value):
        """ Setter method """
        if not isinstance(value, tuple) or len(value) != 2
        or type(value[0]) is not int or value[0] < 0
        or type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

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
            for k in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                for l in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print("")
