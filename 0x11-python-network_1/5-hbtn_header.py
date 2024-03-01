#!/usr/bin/python3
"""the response header value task"""
import sys
import requests

if __name__ == "__main__":
    the_link = sys.argv[1]

    the_res = requests.get(the_link)
    print(the_res.headers.get("X-Request-Id"))
