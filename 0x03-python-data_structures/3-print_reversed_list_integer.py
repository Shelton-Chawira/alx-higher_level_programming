#!/usr/bin/python3.8
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return

    for i in range(len(my_list) - 1, -1, -1):
        print("{:d}".format(my_list[i]))
