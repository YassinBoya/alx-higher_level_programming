#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    squares = list(map(lambda row: list(map(lambda num: num * num, row)), matrix))
    return squares
