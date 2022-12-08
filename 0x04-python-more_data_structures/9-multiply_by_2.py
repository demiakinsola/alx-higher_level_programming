#!/usr/bin/python3

# This function returns a new dictionary with all values multiplied by 2.
def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    for key, value in new_dict.items():
        value * 2
    return new_dict
