#!/usr/bin/python3
for i in range(9):
    for j in range(1 + i, 10):
        print('{}{}'.format(i, j), end=', ' if i < 8 or j <9 else '')
print()
