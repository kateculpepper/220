"""
Name: <Kate Culpepper>
<lab 10>.py

Problem: <This assignment runs a program the integrates to knew class types, door and button, and
 displays the door game in a graphics window>

Certification of Authenticity:

I certify that this assignment is my own work, but I discussed it with: <Kate Culpepper>
"""




from door import Door
from button import Button
from graphics import *


def main():
    width_px = 700
    height_px = 700
    win = GraphWin("test", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)
    button_rec = Rectangle(Point(3.0, 9.0), Point(7.0, 8.0))

    button = Button(button_rec, "exit")
    button.draw(win)

    door = Door(Rectangle(Point(3.0, 7), Point(7, 0)), "closed")
    door.color_door('Red')

    door.draw(win)
    click = False
    while True:
        mouse = win.getMouse()
        if  button.is_clicked(mouse) == True:
            break
        elif door.is_clicked(mouse) and click == False:
            click = True
            door.open("white", "opened")
        elif door.is_clicked(mouse) and click == True:
            click = False
            door.close("red", "closed")





    win.close()


if __name__ == '__main__':
    main()
