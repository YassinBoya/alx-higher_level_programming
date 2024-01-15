#!/usr/bin/python3
"""Defines the base class"""


class Base:
    """
    Representation of Base class

    This class will be the “base” of all other classes in this project

    __nb_objects : private class attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        inizialize a new base

        args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects