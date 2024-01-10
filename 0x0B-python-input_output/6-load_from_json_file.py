#!/usr/bin/python3
"""defines the load_from_json_file function"""
import json


def load_from_json_file(filename):
    with open(filename, 'r') as file:
        return json.load(file)
