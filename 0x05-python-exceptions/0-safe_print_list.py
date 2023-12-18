#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        if (x > 5):
            x = 5
        for i in range(x):
            print("{}".format(my_list[i]), end="")
        print()    
    except IndexError:
        pass
    return (x)    
