#!/usr/bin/python3
"""Status check"""
import requests

if __name__ == "__main__":
    the_res = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(the_res.text)))
    print("\t- content: {}".format(the_res.text))
