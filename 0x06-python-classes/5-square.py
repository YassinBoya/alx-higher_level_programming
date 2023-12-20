#!/usr/bin/python3

"""Define a Square."""


class Square:
    """Represent a Square.

    Attributes:
        size: size of a square (1 side).
    """

    def __init__(self, size=0):

        """Initiaize a new Square.

        Args:
            size (int): the size of a new square.
        """
        self.__size = size

    def area(self):
        """Return the current square area."""
        return (self.__size * self.__size)

    @property
    def size(self):
        """get the square size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for row in range(self.__size):
                for col in range(self.__size):
                    print("#", end="")
                print("")
