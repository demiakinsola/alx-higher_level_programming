#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx > (len(my_list) - 1):
        return my_list
# Used -1 because index starts from 0 but length from 1.
    else:
        my_list[idx] = element