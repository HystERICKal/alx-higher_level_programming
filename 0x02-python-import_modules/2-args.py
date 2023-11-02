#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    l_o_a = len(sys.argv)
    if l_o_a == 1:
        print("{0} arguments.".format(l_o_a - 1))
    elif l_o_a == 2:
        print("{0} argument:".format(l_o_a - 1))
    else:
        print("{0} arguments:".format(l_o_a - 1))
    for h in range(1, l_o_a):
        print("{0}: {1}".format(h, sys.argv[h]))
