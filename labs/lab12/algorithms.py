"""
Name: <Kate Culpepper>
<lab 12>.py

Problem: <This assignment runs a program with a series of different functions>

Certification of Authenticity:

I certify that this assignment is my own work>
"""


def read_data(filename):
    open_file = open(filename, 'r')
    list1 = open_file.readlines()
    list2 = []
    i = 0
    while i < len(list1):
        line = list1[i].split(' ')
        j = 0
        while j < len(line):
            list2.append(line[j].strip())
            j = j + 1
        i = i + 1
    open_file.close()
    return list2


def is_in_linear(search_val, values):
    i = 0
    while i < len(values):
        if search_val == values[i]:
            return True
        else:
            i += 1
    return False
