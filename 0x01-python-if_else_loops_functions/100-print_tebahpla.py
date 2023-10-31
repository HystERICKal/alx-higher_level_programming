#!/usr/bin/python3
for r in range(122, 96, -1):
    if r % 2:
        r = r - 32
    print("{:c}".format(r), end="")
