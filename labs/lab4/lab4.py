"""
Name: <Kate Culpepper>
<Lab1>.py

Problem: <This program opens a window with a Valentine's Day card that has  an animated arrow, and a greeting. You
click to close the program>

Certification of Authenticity:

I certify that this assignment is my own work <Kate Culpepper>
"""


from graphics import *


def greeting_card():

    card = GraphWin("Valentine's Day Card", 700, 700)
    card.setBackground("Pink")

    heart = Polygon(Point(350, 550), Point(450, 350), Point(250, 350))
    heart.draw(card)
    heart.setFill("Red")
    heart.setOutline("Red")

    heart_circle1 = Circle(Point(300, 350), 50)
    heart_circle1.draw(card)
    heart_circle1.setFill("Red")
    heart_circle1.setOutline("Red")

    heart_circle2 = Circle(Point(400, 350), 50)
    heart_circle2.draw(card)
    heart_circle2.setFill("Red")
    heart_circle2.setOutline("Red")

    greeting = Text(Point(350, 150), "Happy Valentine's Day!<3")
    greeting.setSize(36)
    greeting.setFace("courier")
    greeting.draw(card)

    arrow = Polygon(Point(225, 450), Point(200, 425), Point(200, 475))
    arrow.draw(card)
    arrow.setFill("Purple")

    arrow_2 = Polygon(Point(200, 450), Point(50, 450))
    arrow_2.draw(card)

    arrow_3 = Polygon(Point(100, 450), Point(75, 440), Point(30, 440), Point(50, 450))
    arrow_3.draw(card)
    arrow_3.setFill("Purple")

    arrow_4 = Polygon(Point(100, 450), Point(75, 460), Point(30, 460), Point(50, 450))
    arrow_4.setFill("Purple")
    arrow_4.draw(card)

    for i in range(15):
        arrow.move(50, 0)
        arrow_2.move(50, 0)
        arrow_3.move(50, 0)
        arrow_4.move(50, 0)
        time.sleep(.5)

    close_2 = Text(Point(350, 650), "click to close ")
    close_2.draw(card)

    card.getMouse()
    card.close()


greeting_card()
