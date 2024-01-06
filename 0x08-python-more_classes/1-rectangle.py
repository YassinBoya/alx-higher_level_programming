#!/usr/bin/python3
"""Define a rectangle class"""


class Rectangle:
    """Represention of the instance object"""

    def __init__(self, width=0, height=0):
        """
        Args:

        width : the width of the new rectangle
        height : the height of the new rectangle

        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Get/Set the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Get/Set the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
