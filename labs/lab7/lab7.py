"""
Name: <Kate Culpepper>
<Lab7.py

Problem: <This program creates two circles of different colors and chooses initial random directions for them to
move. If either circle hits a wall, that circle  moves away from the wall. If
the circles collide, both circles change to the opposite direction. >

Certification of Authenticity:

I certify that this assignment is entirely my own work.

"""

import math
from random import *
from graphics import *


def get_random(move_amount):
    rand_num = randint(-move_amount, move_amount)
    return rand_num


def did_collide(circleball, circleball2):
    distance = math.sqrt(
        ((circleball.getCenter().getX() - circleball2.getCenter().getX()) ** 2) + (
                    (circleball.getCenter().getY() - circleball2.getCenter().getY()) ** 2))
    circle_radius = circleball.getRadius() + circleball2.getRadius()
    return circle_radius >= distance


def hit_vertical(ball, win):
    ball_center_y = ball.getCenter().getY()
    ball_radius = ball.getRadius()

    return ball_center_y <= ball_radius or ball_center_y + ball_radius >= win.getHeight()


def hit_horizontal(ball, win):
    ball_center_x = ball.getCenter().getX()
    ball_radius = ball.getRadius()

    return ball_center_x <= ball_radius or ball_center_x + ball_radius >= win.getWidth()


def get_random_color():
    rand_num = abs(get_random(255))
    rand_num2 = abs(get_random(255))
    rand_num3 = abs(get_random(255))
    circle_color = color_rgb(rand_num, rand_num2, rand_num3)
    return circle_color


def bumper():
    win_width = 400
    win_height = 400
    win = GraphWin("Bumper cars", win_width, win_height)
    win.setBackground("white")

    circle1 = Circle(Point(randint(1, 350), randint(1, 300)), 25)
    circle1.setFill(get_random_color())
    circle1.draw(win)
    circle2 = Circle(Point(randint(1, 350), randint(1, 300)), 25)
    circle2.setFill(get_random_color())
    circle2.draw(win)

    randMoveC1X = randint(1, 5)
    randMoveC1Y = randint(1, 5)
    randMoveC2X = randint(1, 5)
    randMoveC2Y = randint(1, 5)
    while not win.checkMouse():
        circle1.move(randMoveC1X, randMoveC1Y)
        circle2.move(randMoveC2X, randMoveC2Y)
        if did_collide(circle1, circle2):
            randMoveC1X = randMoveC1X * -1
            randMoveC1Y = randMoveC1Y * -1
            randMoveC2X = randMoveC2X * -1
            randMoveC2Y = randMoveC2Y * -1
        if hit_vertical(circle1, win):
            randMoveC1Y = randMoveC1Y * -1
        if hit_vertical(circle2, win):
            randMoveC2Y = randMoveC2Y * -1
        if hit_horizontal(circle1, win):
            randMoveC1X = randMoveC1X * -1
        if hit_horizontal(circle2, win):
            randMoveC2X = randMoveC2X * -1


bumper()
