#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    sum_elem = ()
    tuple_1 = tuple_a + (0, 0)
    tuple_2 = tuple_b + (0, 0)
    for i in range(2):
        sum_elem += (tuple_1[i] + tuple_2[i],)
    return(sum_elem)
