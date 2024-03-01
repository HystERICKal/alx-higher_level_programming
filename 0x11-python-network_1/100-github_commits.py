#!/usr/bin/python3
"""listing commits"""
import sys
import requests

if __name__ == "__main__":
    the_link = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    the_res = requests.get(the_link)
    temp = the_res.json()
    try:
        x = 0
        while x < 10:
            print("{}: {}".format(
                temp[x].get("sha"),
                temp[x].get("commit").get("author").get("name")))
            x += 1
    except IndexError:
        pass
