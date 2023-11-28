#!/usr/bin/python3
def pow(a, b):
    power_res = 1
    if b < 0:
        a = 1 / a
        b = abs(b)
    for i in range(b):
        power_res = power_res * a
    return (power_res)
