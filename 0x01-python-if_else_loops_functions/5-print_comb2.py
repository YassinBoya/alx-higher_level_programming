#!/usr/bin/python3
for i in range(0, 100, 1):
    if i == 98:
        print('{:02}'.format(i))
        break
    print('{:02}'.format(i), end=', ')
