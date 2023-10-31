#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    ending_digit = number % -10 #handle negatives
elif number >= 0:
    ending_digit = number % 10 #handle positives
if ending_digit > 5:
    print(f"Last digit of {number} is {ending_digit} and is greater than 5")
elif ending_digit == 0:
    print(f"Last digit of {number} is {ending_digit} and is 0")
else:
    print(f"Last digit of {number} is {ending_digit} and is less than 6 and not 0")
