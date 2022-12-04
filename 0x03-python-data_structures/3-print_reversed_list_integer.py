#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    length = len(my_list) - 1
    index = 0
# Length starts counting from 1 and not 0
    while length <= index:
        print('{:d}'.format(my_list[length]))
        length -= 1
