#!/usr/bin/python3
# Author: Shelton Anotida Chawira
for num in range(100):
    print("{:02d}".format(num), end=", " if num < 99 else "\n")
