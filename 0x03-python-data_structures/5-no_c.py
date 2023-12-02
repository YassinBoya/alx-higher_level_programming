#!/usr/bin/python3
'''
def no_c(my_string):
    new_str = ""
    if my_string:
        for char in my_string:
            if char != 'C' and char != 'c':
                new_str += char
    return(new_str)
'''


def no_c(my_string):
    new_string = my_string.translate({ord(i): None for i in 'cC'})
    return new_string
