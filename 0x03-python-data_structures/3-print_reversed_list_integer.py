#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    index = len(my_list) - 1
    for _ in my_list:
        print('{:d}'.format(my_list[index]))
        index -= 1


'''
def print_reversed_list_integer(my_list=[]):
    for item in reversed(my_list):
        print('{:d}'.format(item))
'''
