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

    @property
    def size(self):
        """get the square size"""
        return(self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return (self.__size * self.__size)
