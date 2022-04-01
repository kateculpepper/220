
"""
Name: <kate Culpepper>
<hw 10>.py

Problem: <In this program it runs a number of differetn functions, related to dofferent sequences
 this program also include a sphere class and a face class>

Certification of Authenticity:

I certify that this assignment is entirely my own work.

"""

from graphics import *
from face import Face


f = f n-1 + fn-2

def fibonacci(n):
    if n < 1:
        return None
    elif n == 1 or n == 2:
        return 1
    elif n == 0:
        return 0
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def double_investment(principle, rate):
    A = principle * (1 + rate)
    year = 1
    a_total = A
    acc = principle

    while acc < principle * 2:
        a_total = (principle * (1 + rate))
        acc = acc + a_total
        year = year + 1

    return year
    pass


def syracuse(n):
    syr_list = [n]
    while n != 1:
        if n % 2 == 0:
            n = (n // 2)
            syr_list.append(n)
        else:
            n = (3 * n + 1)
            syr_list.append(n)

    return syr_list
    pass


def is_prime(n):
    i = 2
    while i < n:
        if n % i == 0:
            return False
        else:
            i = i + 1
    return True


def goldbach(n):  # output: [prime, prime]

    if n % 2 != 0:
        return None

    gold_list = []

    num_1 = 2
    num_2 = 2
    if num_1 + num_2 == n:
        gold_list.append(num_1)
        gold_list.append(num_2)
        return gold_list
    acc = 3
    num_1 = 3
    num_2 = 3
    while num_1 + num_2 < n :

        while num_1 + num_2 < n:
            if num_1 + num_2 == n:
                break
            if is_prime(num_2 + 2):
                num_2 = num_2 + 2
            else:
                num_2 = num_2 + 4
        num_2 = num_1
    if num_1 + num_2 == n:
        gold_list.append(num_1)
        gold_list.append(num_2)
        return gold_list
    else:
        return None


def main():
    width_px = 900
    height_px = 900
    window = GraphWin("test", width_px, height_px)
    width = 10
    height = 10
    window.setCoords(0, 0, width, height)

    face = Face(window, Point(5, 5), 4)
    face.wink(window, Point(5, 5), 4)
    window.getMouse()
    window.close()


if __name__ == '__main__':
    # main()
    print(is_prime(9))
