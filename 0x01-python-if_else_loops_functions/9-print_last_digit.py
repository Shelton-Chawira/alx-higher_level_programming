#!/usr/bin/python3

def print_last_digit(number):
    last_digit = abs(number) % 10  # Get the last digit using modulo
    print(last_digit, end="")
    return last_digit
