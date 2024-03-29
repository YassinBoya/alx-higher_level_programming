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
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @property
    def height(self):
        """Set/get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @property
    def x(self):
        """Set/get the coordinate x of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, x):
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
        """Set/get the coordinate y of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, y):
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

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
        """Update the Rectangle.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
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

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
