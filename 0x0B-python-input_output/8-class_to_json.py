#!/usr/bin/python3
"""defines the class_to_json function"""


def class_to_json(obj):
    """Return the dictionary represntation of a simple data structure."""
    return obj.__dict__
