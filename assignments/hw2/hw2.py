"""
Name: <Kate Culpepper>
<HomeWork1>.py

Problem: <This assignment runs a series of different programs that allow you to find
the sum of threes, a multiplication table, the area of a triangle, the sum of squared numbers, and the a program that manually finds the power >

Certification of Authenticity:

I certify that this assignment is entirely my own work.

"""
import math


def sum_of_threes():
    upper_bound = eval(input(" What is the upper bound? : "))
    s_acc = 0

    for i in range(0, upper_bound + 1, 3):
        s_acc = s_acc + i

    print("sum of threes is :", s_acc)


def multiplication_table():
    for i in range(1, 11):
        for j in range(1, 11):
            print(i * j, end="\t")
        print("")


def triangle_area():
    side_a = eval(input("Enter side a length: "))
    side_b = eval(input("Enter side b length: "))
    side_c = eval(input("enter side c length: "))

    s_value = (side_a + side_b + side_c) / 2
    a_value = s_value * ((s_value - side_a) * (s_value - side_b) * (s_value - side_c))
    area = math.sqrt(a_value)

    print("Area is: ", area)


def sum_squares():
    low_range = eval(input("Enter lower range: "))
    up_range = eval(input("Enter upper range: "))

    s_of_sqr_acc = 0

    for i in range(low_range, up_range + 1):
        multiply_var = i * i
        s_of_sqr_acc = s_of_sqr_acc + multiply_var

    print(s_of_sqr_acc)


def power():
    base = eval(input("Enter base: "))
    exponent = eval(input("Enter exponent: "))

    power_acc = 1

    for i in range(1, exponent + 1):
        power_acc = power_acc * base

    print(base, "^", exponent, "=", power_acc)


if __name__ == '__main__':
   # sum_of_threes()
   # triangle_area()
   # sum_squares()
    multiplication_table()
   # power()
