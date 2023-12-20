#!/usr/bin/python3

"""Define a Square."""


class Square:
    """Represent a Square.

    Attributes:
        size: size of a square (1 side).
    """

    def __init__(self, size=0, position=(0, 0)):

        """Initiaize a new Square.

        Args:
            size (int): the size of a new square.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """get the square position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple)
                or len(value) != 2
                or not all(isinstance(num, int) for num in value)
                or not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for row in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ",  end="")
                for col in range(self.__size):
                    print("#", end="")
                print()
