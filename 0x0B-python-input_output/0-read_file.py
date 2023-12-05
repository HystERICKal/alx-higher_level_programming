#!/usr/bin/python3
""" Function that reads a file """


def read_file(filename=""):
    """ Function that reads a file """
    with open(filename) as f:
        while f:
            sentence = f.readline()
            print(sentence, end='')
            if sentence == "":
                break
        f.close()
