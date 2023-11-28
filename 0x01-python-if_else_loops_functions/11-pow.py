#!/usr/bin/python3
def pow(a, b):
    power_res = 1
    if b >= 0:
        for _ in range(b):
            power_res *= a
    else:
        for _ in range(abs(b)):
            power_res /= a
    return round(power_res, 20)
