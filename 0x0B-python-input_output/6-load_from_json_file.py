#!/usr/bin/python3
"""defines the load_from_json_file function"""
import json


def load_from_json_file(filename):
    """Create a Python object from a JSON file."""
    with open(filename, 'r') as file:
        return json.load(file)
