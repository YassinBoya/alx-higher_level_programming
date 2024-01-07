#!/usr/bin/python3
"""Define a rectangle class"""


class Rectangle:
    """Represention of the instance object"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
        Args:

        width : the width of the new rectangle
        height : the height of the new rectangle

        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Return the area of a rectangle"""

        return self.width * self.height

    def perimeter(self):
        """Return the perimetre of a rectangle"""

        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        stringDisplaySign = ""
        """Print the # sign depends on the width and height"""

        if self.width == 0 or self.height == 0:
            return ""
        for i in range(self.height):
            for j in range(self.width):
                stringDisplaySign += str(self.print_symbol)
            if i < self.height - 1:
                stringDisplaySign += "\n"
        return stringDisplaySign

    def __repr__(self):
        """return a string representation of the rectangle"""

        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """
        Print the message Bye rectangle...
        when an instance of Rectangle is deleted
        """
        print(f"Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
