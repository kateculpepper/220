"""
Name: <Kate Culpepper>
<lab 10>.py

Problem: <This assignment runs a program the integrates to knew class types, door and button, and
 displays the door game in a graphics window>

Certification of Authenticity:

I certify that this assignment is my own work, but I discussed it with: <Kate Culpepper>
"""


from graphics import *


class Button:
    def __init__(self, shape, label):
        self.shape = shape
        self.text = Text(Point(shape.getCenter().getX(), shape.getCenter().getY()), label)

    def get_label(self):
        return self.text

    def set_label(self, label):
        new_label = label
        self.text.setText(new_label)

    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self, point):
        if point == None:
            return False

        point_x = point.getX()
        point_y = point.getY()
        shape_p1 = self.shape.getP1()
        shape_p2 = self.shape.getP2()


        if shape_p1.getX() <= point_x <= shape_p2.getX() and shape_p1.getY() <= point_y <= shape_p2.getY():
            return True
        else:
            return False

    def color_button(self, color):
        self.shape.setFill(color)
