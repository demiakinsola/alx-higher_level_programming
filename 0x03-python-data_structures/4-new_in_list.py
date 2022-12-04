#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    create_list = my_list
# Make a copy of the original list.
    if idx < 0:
        return my_list
    elif idx > (len(my_list) - 1):
        return my_list
# Length starts counting from 1 not 0.
    else:
        create[idx] = element
        return create_list
