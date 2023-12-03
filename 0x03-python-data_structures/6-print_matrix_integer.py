#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    space = ""
    if matrix:
        for row in matrix:
            for col_i in row:
                if col_i != row[-1]:
                    space = " "
                print('{:d}'.format(col_i), end=space)
            print()
