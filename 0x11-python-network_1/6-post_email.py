#!/usr/bin/python3
"""Lets post email"""
import sys
import requests


if __name__ == "__main__":

    the_res = requests.post(sys.argv[1], data={"email": sys.argv[2]})
    print(the_res.text)
