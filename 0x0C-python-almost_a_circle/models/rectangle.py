#!/usr/bin/python3
"""Defines the Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Representation of Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Class Rectangle inherits from Base

        Args :
            width (int): the width of the new rectangle
            height (int): the height of the new rectangle
            x (int): the coordinate x of the new rectangle
            y (int): the coordinate y of the new rectangle
            id (int): the id of the new rectangle

        Raises:
            TypeError: If any of width, height, x, or y is not an int.
            ValueError: if either of width or height <= 0
            ValueError: if either x or y < 0

        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Set/get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        """Set/get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def x(self):
        """Set/get the coordinate x of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        """Set/get the coordinate y of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y
