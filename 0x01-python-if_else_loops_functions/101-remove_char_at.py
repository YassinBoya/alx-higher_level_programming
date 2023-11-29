#!/usr/bin/python3
def remove_char_at(s, n):
    i = 0
    clean_str = ''
    while i < len(s):
        if i != n:
            clean_str += s[i]
        i += 1
    return (clean_str)
