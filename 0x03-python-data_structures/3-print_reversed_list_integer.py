#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    index = 0
# Length starts counting from 1 and not 0
    while index < len(my_list):
        print('{:d}'.format(my_list[index]))
        index += 1
