"""
Name: <Kate Culpepper>
<HW8>.py

Problem: <This program runs a series of functions, that adds 10 to each item in a list
sures each item within a list, sum a list of numbers, changes a string of numbers
into floats, sets parameters to athletes, and calculates if a year is a leap year, the final 
function displays if two circles overlap >

Certification of Authenticity:

I certify that this assignment is entirely my own work.

"""
from graphics import *
import math


def add_ten(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] + 10


def square_each(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2


def sum_list(nums):
    add_sum = 0
    for i in nums:
        add_sum = add_sum + i
    return add_sum


def to_numbers(nums):
    for i in range(len(nums)):
        nums[i] = float(nums[i])


def sum_of_squares(nums):
    for i in range(len(nums)):
        split_string = nums[i].split(', ')
        to_numbers(split_string)
        square_each(split_string)
        nums[i] = sum_list(split_string)
    return nums


def starter(weight, wins):
    if 150 <= weight < 160 and wins >= 5:
        return True
    elif weight > 199 or wins > 20:
        return True
    else:
        return False


def leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


def circle_overlap():
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)

    center = win.getMouse()
    circumference_point = win.getMouse()
    radius = math.sqrt(
        (center.getX() - circumference_point.getX()) ** 2 + (center.getY() - circumference_point.getY()) ** 2)
    circle_one = Circle(center, radius)
    circle_one.setFill("light blue")
    circle_one.draw(win)

    center_two = win.getMouse()
    circumference_point_two = win.getMouse()
    radius_two = math.sqrt((center_two.getX() - circumference_point_two.getX()) ** 2 + (
            center_two.getY() - circumference_point_two.getY()) ** 2)
    circle_two = Circle(center_two, radius_two)
    circle_two.setFill("Red")
    circle_two.draw(win)

    if did_overlap(circle_one, circle_two):
        text = Text(Point(5, 5), "The circles overlap")
        text.draw(win)
    else:
        text_2 = Text(Point(5, 5), "The circles do not overlap")
        text_2.draw(win)
    close_text = Text(Point(5, 2), "Click again to close")
    close_text.draw(win)

    win.getMouse()


def did_overlap(circle_one, circle_two):
    distance = math.sqrt(
        ((circle_one.getCenter().getX() - circle_two.getCenter().getX()) ** 2) + (
                (circle_one.getCenter().getY() - circle_two.getCenter().getY()) ** 2))
    circle_radius = circle_one.getRadius() + circle_two.getRadius()
    return circle_radius >= distance


if __name__ == '__main__':
    add_ten([1, 2, 3])
    sum_list([1, 2, 3])
    circle_overlap()
    sum_of_squares(["3, 7.2, 9", "2, 2.3"])
    square_each()
    to_numbers()
    did_overlap()
    starter()
    leap_year()

