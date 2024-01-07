#!/usr/bin/python3
"""defines the add_integer function"""


def add_integer(a, b=98):
    """
    Represents the add_integer function.

    Args:
        a (int or float): The first number for the addition operation.
        b (int or float): The second number
        for the addition operation. Default is 98.

    Raises:
        TypeError: If either a or b is not an integer or float.

    Returns:
        int: The result of the addition of a and b.
    """
    if ((not isinstance(a, int)) and (not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int)) and (not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
