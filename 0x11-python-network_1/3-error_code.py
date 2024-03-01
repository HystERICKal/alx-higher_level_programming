#!/usr/bin/python3
"""the err code"""

if __name__ == '__main__':
    import sys
    from urllib import request, error

    argv = sys.argv
    the_link = argv[1]
    try:
        with request.urlopen(the_link) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as err:
        print("Error code: {}".format(err.status))
