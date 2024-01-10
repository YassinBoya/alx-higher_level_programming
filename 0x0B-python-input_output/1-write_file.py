#!/usr/bin/python3
"""defines a write file function"""


def write_file(filename="", text=""):
    """write the contents of a UTF8 text into a file
    and return the number of characters written."""
    with open(filename, 'w', encoding="utf-8") as file:
        file.write(text)
    return (len(text))
