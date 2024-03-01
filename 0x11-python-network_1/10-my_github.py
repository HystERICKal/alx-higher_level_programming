#!/usr/bin/python3
"""this is my git"""
import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    credentials = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    the_res = requests.get("https://api.github.com/user", auth=credentials)
    print(the_res.json().get("id"))
