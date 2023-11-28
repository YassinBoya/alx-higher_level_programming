#!/usr/bin/python3
def pow(a, b):
    power_res = 1
    if b < 0:
        a = 1 / a
        b = abs(b)
    for _ in range(b):
        power_res *= a
    if b < 0:
        power_res = 1 / power_res
    return round(power_res, 15)
