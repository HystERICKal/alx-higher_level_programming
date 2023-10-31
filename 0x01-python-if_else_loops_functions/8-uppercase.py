#!/usr/bin/python3
def uppercase(str):
    n = 0
    while n < len(str):
        g = str[n]
        if (ord(str[n]) >= 97 and ord(str[n]) <= 122):
            g = chr(ord(str[n]) - 32)
        print("{:s}".format(g), end="")
        n += 1
    print()
