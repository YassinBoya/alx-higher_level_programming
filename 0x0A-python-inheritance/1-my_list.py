#!/usr/bin/python3
"""defines the lookup function"""


class MyList(list):
    """Representation of sorting a built-in list class"""
    def print_sorted(self):
        """prints the list, sorted in ascending way"""
        print(sorted(self))
