#!/usr/bin/python3
def no_c(my_string):
    new_str = []
    for char in my_string:
        if char != 'C' and char != 'c':
            new_str.extend(char)
    res_str = ''.join(new_str)
    return(res_str)
