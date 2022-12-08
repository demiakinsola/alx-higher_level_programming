#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    for key, value in sorted(a_dictionary.items(), key=lambda x: x[0]): 
# This is to get the keys and values sorted by x[0](i.e. keys)
        print('{}: {}'.format(key, value))
