#!/usr/bin/python3
def fizzbuzz():
    t = 1
    while t < 101:
        if t % 3 == 0 and t % 5 == 0:
            print("FizzBuzz ", end="")
        elif t % 3 == 0:
            print("Fizz ", end="")
        elif t % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{:d} ".format(t), end="")
        t += 1
