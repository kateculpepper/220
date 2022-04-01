from graphics import *
from face import Face


# f = f n-1 + fn-2

def fibonacci(n):
    if n < 1:
        return None
    elif n == 1 or n == 2:
        return 1
    elif n == 0:
        return 0
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
# am i allowed to use recursion,

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


def goldbach(n):  # output: [prime, prime]

gold_list: []
    while n > 2:
        if n % 2 == 0:
            return True
        else:
            return None
pass

def main():
    width_px = 700
    height_px = 700
    window = GraphWin("test", width_px, height_px)
    width = 10
    height = 10
    window.setCoords(0, 0, width, height)

    Face(window, Point(5, 5), 4)
    window.getMouse()
    window.close()


if __name__ == '__main__':
    main()
