#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        the_divisor = 0
        the_dividend = 0

        for pair in my_list:
            the_dividend = the_dividend + pair[0] * pair[1]
            the_divisor = the_divisor + pair[1]

        return (the_dividend / the_divisor)
    else:
        return 0
