"""
Name: <Kate Culpepper>
<lab 13>.py

Problem: <This assignment runs a program with a series of different functions>

Certification of Authenticity:

I certify that this assignment is my own work>

read_data() should take one parameter, the file name, not hardcode in a file.
read_data() gets stuck in an infinite loop
read_data() does not process each line in any way, so the output is a list of strings, each containing a full line's worth of numbers
"""

from graphics import *


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


def selection_sort(values):
    list_nums = len(values)
    for low_num in range(list_nums - 1):
        num = low_num
        for i in range(low_num + 1, list_nums):
            if values[i] < values[num]:
                num = i
        values[low_num], values[num] = values[num], values[low_num]


def calc_area(rect):
    p1X = rect.getP1().getX()
    p1Y = rect.getP1().getY()
    p2X = rect.getP2().getX()
    p2Y = rect.getP2().getY()
    length = abs(p1X - p2X)
    width = abs(p1Y - p2Y)
    return length * width


def rect_sort(rectangles):
    list_nums = len(rectangles)
    for low_num in range(list_nums - 1):
        num = low_num
        for i in range(low_num + 1, list_nums):
            if calc_area(rectangles[i]) < calc_area(rectangles[num]):
                num = i
        rectangles[low_num], rectangles[num] = rectangles[num], rectangles[low_num]


if __name__ == '__main__':
    print(read_data('data_sorted.txt'))

    vList = [3,2,4,5,1]
    print(is_in_linear(4, vList))
    print("Unsorted: ", vList)
    selection_sort(vList)
    print("Sorted: ", vList)

    rec = Rectangle(Point(0, 0), Point(20, 20))
    rec2 = Rectangle(Point(0, 0), Point(10, 10))
    rec3 = Rectangle(Point(0, 0), Point(5, 5))
    rects = [rec, rec3, rec2]
    print(rects)
    rect_sort(rects)
    print(rects)
