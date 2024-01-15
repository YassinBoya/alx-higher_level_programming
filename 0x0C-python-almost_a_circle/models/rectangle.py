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
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Set/get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Set/get the coordinate x of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Set/get the coordinate y of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return the area of a rectangle"""

        return self.width * self.height

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""

        if self.width == 0 or self.height == 0:
            print("")
            return
        for iy in range(self.y):
            print("")
        for i in range(self.height):
            for jx in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print(f"#", end="")
            print()

    def __str__(self):

        """returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""

        return (f"[Rectangle] ({self.id}) {self.x}/{self.y} - \
{self.width}/{self.height}")

    def update(self, *args, **kwargs):
        for par, arg in enumerate(args):
            if arg is None:
                self.__init__(self.width, self.height, self.x, self.y)
            if par == 0:
                self.id = arg
            elif par == 1:
                self.width = arg
            elif par == 2:
                self.height = arg
            elif par == 3:
                self.x = arg
            elif par == 4:
                self.y = arg
