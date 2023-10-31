#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        ending_dig = (-number % 10)
    elif number >= 0:
        ending_dig = number % 10
    print("{:d}".format(ending_dig), end="")
    return ending_dig
