#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squares = [[num * num for num in row] for row in matrix]
    return (squares)
