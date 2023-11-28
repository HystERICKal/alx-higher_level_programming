#!/usr/bin/python3
""" Function For text indentation """


def text_indentation(text):
    """ Function For text indentation """

    chrct_arr = ['.', '?', ':']
    check_str_instance = isinstance(text, str)
    x = 0

    if not check_str_instance:
        raise TypeError('text must be a string')
    if text == "":  # empty text
        print('')
        return
    if text is None:  # no text entered
        raise EOFError('you must enter text to use the function')

    while x < len(chrct_arr):
        if chrct_arr[x] in text:
            text = text.replace(chrct_arr[x], '\n\n')
        x += 1
    print(text)
