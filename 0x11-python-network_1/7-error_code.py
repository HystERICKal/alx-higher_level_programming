#!/usr/bin/python3
"""printing err code"""
import sys
import requests

if __name__ == "__main__":

    the_res = requests.get(sys.argv[1])
    if the_res.status_code >= 400:
        print("Error code: {}".format(the_res.status_code))
    else:
        print(the_res.text)
