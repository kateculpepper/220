"""
Name: <Kate Culpepper>
<lab 11>.py

Problem: <This assignment runs a program with a series of different functions>

Certification of Authenticity:

I certify that this assignment is my own work>
"""


def read_data():
    open_file = open('data_sorted.txt', 'r')
    list = []
    while list == list:
        line = open_file.readline()
        list.append(line)
    open_file.close()


def is_in_linear(search_val, values):
    while i < len(values):
        if search_val in values:
            return True
        else:
            return False
