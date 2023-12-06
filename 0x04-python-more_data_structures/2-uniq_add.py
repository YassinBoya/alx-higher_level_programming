#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_list = set()
    unique_list = [num for num in my_list if num not in unique_list
                   and not unique_list.add(num)]
    return sum(unique_list)
