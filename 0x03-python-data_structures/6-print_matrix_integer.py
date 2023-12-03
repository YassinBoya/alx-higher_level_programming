#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in matrix:
            for col_i in row:
                print('{:d}'.format(col_i), end=" " if col_i != row[-1] else "")
            print()
