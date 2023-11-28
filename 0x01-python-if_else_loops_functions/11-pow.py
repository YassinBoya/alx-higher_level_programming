#!/usr/bin/python3
def pow(a, b):
    if b == 0:
        return 1
    power_res = 1
    if b < 0:
        a = 1 / a
        b = abs(b)
    for _ in range(b):
        power_res *= a
    return round(power_res, 15)
