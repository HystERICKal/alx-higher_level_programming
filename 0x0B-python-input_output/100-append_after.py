#!/usr/bin/python3
"""The search and update function"""


def append_after(filename="", search_string="", new_string=""):
    """The search and update function"""
    word = ""
    with open(filename) as the_file:
        while the_file:
            sentence = the_file.readline()
            word = word + sentence
            if search_string in sentence:
                word = word + new_string
            if sentence == "":
                break
        the_file.close()
    with open(filename, "w") as the_file:
        the_file.write(word)
