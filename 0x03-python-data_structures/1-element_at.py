#!/usr/bin/python3

def element_at(my_list, idx):
    if idx < 0:
        return None
    elif idx > (len(my_list) - 1):
        return None
# Used -1 because index starts from 0 but length from 1.
    else:
        return my_list[idx]
