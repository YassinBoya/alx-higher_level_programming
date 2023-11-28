#!/usr/bin/python3
def uppercase(str):
    uppercase_str = ""
    for c in str:
        if 'a' <= c <= 'z':
            uppercase_char = chr(ord(c) - ord('a') + ord('A'))
            uppercase_str += uppercase_char
        else:
            uppercase_str += c
    return (print('{}'.format(uppercase_str)))

