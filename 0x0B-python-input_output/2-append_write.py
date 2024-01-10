#!/usr/bin/python3
"""defines teh append file function"""


def append_write(filename="", text=""):
    """open a file for appending text into it.
    If the file doesn't exist, it will be created."""

    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)
    return (len(text))
