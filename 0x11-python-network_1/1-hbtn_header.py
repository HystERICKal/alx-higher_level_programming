#!/usr/bin/python3
"""take in url and send request to it"""
import sys
import urllib.request

if __name__ == "__main__":

    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.headers["X-Request-Id"])
