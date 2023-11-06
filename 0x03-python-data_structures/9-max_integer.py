#!/usr/bin/python3
def max_integer(my_list=[]):
    largest_val = my_list[0]  # make first element largest
    if my_list:  # if list exists
        for curr_val in my_list:  # loop through list
            if curr_val > largest_val:  # looking for a larger value
                largest_val = curr_val  # then update largest_val
            else:
                continue
        return largest_val
    return None
