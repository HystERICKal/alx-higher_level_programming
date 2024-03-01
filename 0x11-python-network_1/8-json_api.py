#!/usr/bin/python3
"""the search API task"""
import sys
import requests

if __name__ == "__main__":
    temp = "" if len(sys.argv) == 1 else sys.argv[1]
    the_res = requests.post("http://0.0.0.0:5000/search_user",
                            data={"q": temp})

    try:
        complete_res = the_res.json()
        if complete_res == {}:
            print("No result")
        else:
            print("[{}] {}".format(complete_res.get("id"),
                                   complete_res.get("name")))
    except ValueError:
        print("Not a valid JSON")
