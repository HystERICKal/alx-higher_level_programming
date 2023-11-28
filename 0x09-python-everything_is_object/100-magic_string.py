#!/usr/bin/python3
def magic_string(temp=[0]):
    temp[0] += 1
    return "BestSchool" + (", BestSchool" * (temp[0] - 1))
