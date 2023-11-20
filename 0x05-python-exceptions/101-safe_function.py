#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        func_reslt = fct(*args)  # executel safely
        return func_reslt  # result of function
    except Exception as err:  # error
        print("Exception: {}".format(err), file=sys.stderr)
        return None
