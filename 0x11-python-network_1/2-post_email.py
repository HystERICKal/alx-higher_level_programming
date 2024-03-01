#!/usr/bin/python3
'''let's Post email'''
from sys import argv
from urllib.request import urlopen, Request
from urllib.parse import urlencode

if __name__ == '__main__':
    the_link = argv[1]
    address = {'email': argv[2]}
    info = urlencode(address).encode('ascii')
    temp = Request(the_link, info)
    with urlopen(temp) as res:
        print(res.read().decode('utf-8'))
