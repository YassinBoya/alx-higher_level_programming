#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in matrix:
            for col_i in row:
                space = ""
                if col_i != row[-1]:
                    space = " "
                print('{:d}'.format(col_i), end=space)
            print()
