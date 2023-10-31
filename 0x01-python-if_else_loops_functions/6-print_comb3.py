#!/usr/bin/python3
for m in range(9):
    for y in range(m + 1, 10):
        if m * 10 + y < 89:
            print("{:d}{:d}".format(m, y), end=", ")
print("{:d}".format(89))
