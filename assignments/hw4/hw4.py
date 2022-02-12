"""
Name: <Kate Culpepper>
<Homewowrk_4>.py

Problem: <in this it was several functions, it lets the user choose placement of squares, find the pereimeter and
area of a rectangle drawn by the user, calculate the radius of a circle made my the user, anc calculates pi>

Certification of Authenticity:

I certify that this assignment is entirely my own work.

"""
import math

from graphics import *
from math import *


def squares():
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Clicks", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to move the square")
    instructions.draw(win)

    # builds a square
    shape = Rectangle(Point(50, 50), Point(100, 100))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the circle
    for i in range(num_clicks):
        click = win.getMouse()
        center = shape.getCenter()  # center of circle

        # move amount is distance from center of circle to the
        # point where the user clicked
        change_x = click.getX() - center.getX()
        change_y = click.getY() - center.getY()
        shape_copy = shape.clone()
        shape_copy.move(change_x, change_y)
        shape_copy.draw(win)

    inst_pt_2 = Point(200, 200)
    instructions_2 = Text(inst_pt_2, "Click again to exit")
    instructions_2.draw(win)

    win.getMouse()
    win.close()


def rectangle():
    win = GraphWin("Rectangle", 400, 400)
    pt_1 = win.getMouse()
    pt_1.draw(win)
    pt_2 = win.getMouse()
    pt_1.undraw()
    line = Rectangle(pt_1, pt_2)
    line.draw(win)

    length = abs(pt_2.getY() - pt_1.getY())
    width = abs(pt_2.getX() - pt_1.getX())
    area = length * width
    perimeter = 2 * (length + width)

    text_p = Text(Point(200, 350), "Perimeter :")
    text_p.draw(win)
    text_p2 = Text(Point(250, 350), " ")
    text_p2.setText(perimeter)
    text_p2.draw(win)
    text_a = Text(Point(200, 360), "Area :")
    text_a.draw(win)
    text_a2 = Text(Point(250, 360), "")
    text_a2.setText(area)
    text_a2.draw(win)

    instr_point = Point(200, 200)
    instructions = Text(instr_point, "Click again to exit")
    instructions.draw(win)

    win.getMouse()
    win.close()


def circle():
    win = GraphWin('Circle', 400, 400)

    center = win.getMouse()
    point = win.getMouse()

    dx = point.getX() - center.getX()
    dy = point.getY() - center.getY()

    d = sqrt(dx ** 2 + dy ** 2)
    w = Circle(center, d)
    w.draw(win)

    text_r = Text(Point(150, 350), "Area :")
    text_r.draw(win)
    text_r2 = Text(Point(250, 350), " hello world ")
    text_r2.setText(d)
    text_r2.draw(win)
    text_close = Text(Point(200, 200), "click again to close")
    text_close.draw(win)

    win.getMouse()

    win.close()


def pi2():
    n_terms = eval(input("Enter the number of terms to sum:"))

    pi_approx = 0
    operator = 1
    for i in range(1, n_terms + 1):
        pi_approx = pi_approx + (operator * (4 / (i * 2 - 1)))

        operator = operator * -1

    accuracy = abs(math.pi - pi_approx)
    print("pi approximation: ", pi_approx)
    print("Accuracy: ", accuracy)


if __name__ == '__main__':
    squares()
    rectangle()
    circle()
    pi2()
