"""
Name: <Kate Culpepper>
<Lab5.py

Problem: <in this it was several functions, it gets teh area and perimeter of a triangle drawn by the user
lets the user color a circle five times, process a string and a list in different ways, sums the numbers in a series
and builds a target>

Certification of Authenticity:

I certify that this assignment is entirely my own work.

"""




import math

from graphics import *



def triangle():
    win = GraphWin("Triangle", 400, 400)
    pt_1 = win.getMouse()
    pt_1.draw(win)
    pt_2 = win.getMouse()
    pt_2.draw(win)
    pt_3 = win.getMouse()
    pt_3.draw(win)
    line = Polygon(pt_1, pt_2, pt_3)
    line.draw(win)

    dy_1 = abs(pt_2.getY() - pt_1.getY())
    dx_1 = abs(pt_2.getX() - pt_1.getX())
    s1_length = math.sqrt((dx_1 ** 2) + (dy_1 ** 2))

    dy_2 = abs(pt_3.getY() - pt_2.getY())
    dx_2 = abs(pt_3.getX() - pt_2.getX())
    s2_length = math.sqrt((dx_2 ** 2) + (dy_2 ** 2))

    dy_3 = abs(pt_1.getY() - pt_3.getY())
    dx_3 = abs(pt_1.getX() - pt_3.getX())
    s3_length = math.sqrt((dx_3 ** 2) + (dy_3 ** 2))

    s = (s1_length + s2_length + s3_length) / 2
    area = math.sqrt(s * ((s - s1_length) * (s - s2_length) * (s - s3_length)))
    perimeter = s1_length + s2_length + s3_length

    text_p = Text(Point(200, 350), "Perimeter :")
    text_p.draw(win)
    text_p2 = Text(Point(300, 350), " ")
    text_p2.setText(perimeter)
    text_p2.draw(win)
    text_a = Text(Point(200, 360), "Area :")
    text_a.draw(win)
    text_a2 = Text(Point(300, 360), "")
    text_a2.setText(area)
    text_a2.draw(win)

    win.getMouse()
    win.close()


triangle()


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")
    red_entry = Entry(Point(win_width / 2 + 10, win_height / 2 + 40), 10)
    red_entry.draw(win)

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")
    green_entry = red_entry.clone()
    green_entry.move(0, 30)
    green_entry.draw(win)

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")
    blue_entry = green_entry.clone()
    blue_entry.move(0, 30)
    blue_entry.draw(win)

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    win.getMouse()

    # the input

    for i in range(5):
        x = red_entry.getText()
        red_inp = eval(x)
        y = green_entry.getText()
        green_inp = eval(y)
        z = blue_entry.getText()
        blue_inp = eval(z)
        shape.setFill(color_rgb(red_inp, green_inp, blue_inp))
        win.getMouse()

    msg_2 = "click again to close "
    inst_2 = Text(Point(200, 50), msg_2)
    inst_2.draw(win)

    # Wait for another click to exit
    win.getMouse()
    win.close()


color_shape()


def process_string():
    user_str = input("Input a string : ")
    print(user_str[0])
    print(user_str[-1])
    print(user_str[2:6])
    a = user_str[0] + user_str[-1]
    print(a)
    b = (user_str[0:3]) * 10
    print(b)

    for i in range(len(user_str)):
        print(user_str[i])

    print(len(user_str))


process_string()


def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    x = values[1] + values[3]
    print(x)
    x = values[0] + values[2]
    print(x)
    x = values[1] + values[1] + values[1] + values[1] + values[1]
    print(x)
    x = [values[2], values[3], values[4]]
    print(x)
    x = [values[2], values[3], values[0]]
    print(x)
    x = [values[2], values[3], float(values[5])]
    print(x)
    x = values[0] + values[2] + float(values[5])
    print(x)
    x = len(values)
    print(x)


process_list()


def another_series():
    n_terms = eval(input("Enter the number of terms to sum:"))
    series = []
    sum = 0
    for i in range(n_terms):
        series.append((i % 3 + 1) * 2)
    for j in range(len(series)):
        sum = sum + series[j]
        print(series[j], end=" ")
    print()
    print("sum = ", sum)


another_series()


def target():
    width = 800
    height = 800
    center_pt= Point(width/2, height /2)
    radius = width /10
    win = GraphWin("target", width, height)

    win.setBackground("black")
    OuterCircle = Circle(center_pt, radius * 5)
    OuterCircle.setFill("white")
    OuterCircle.draw(win)

    OuterCircle1 = Circle(center_pt, radius * 4)
    OuterCircle1.setFill("black")
    OuterCircle1.draw(win)

    OuterCircle2 = Circle(center_pt, radius * 3)
    OuterCircle2.setFill("blue")
    OuterCircle2.draw(win)

    OuterCircle3 = Circle(center_pt, radius * 2)
    OuterCircle3.setFill("red")
    OuterCircle3.draw(win)

    InnerCircle = Circle(center_pt, radius)
    InnerCircle.setFill("yellow")
    InnerCircle.draw(win)

    text_close = Text(center_pt, "click again to close")
    text_close.draw(win)

    win.getMouse()

    win.close()


target()
