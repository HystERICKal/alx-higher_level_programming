#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    totol = 0
    l_o_a = len(sys.argv)
    for y in range(l_o_a):
        if y == 0:
            totol = 0
        else:
            totol = totol + int(sys.argv[y])
    print("{0}".format(totol))
