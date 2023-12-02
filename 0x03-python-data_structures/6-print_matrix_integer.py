#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in matrix:
            for col_i in row:
                if col_i != 0:
                    print(" ", end="")
                print('{:d}'.format(col_i), end="")
            print()
