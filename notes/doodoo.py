head = Circle(Point(3, 7.5), .5)
head.draw(win)

body_line = Line(Point(3, 7), Point(3, 5))
body_line.draw(win)

leg_one = Line(Point(3, 5), Point(2.7, 4))
leg_one.draw(win)

leg_two = Line(Point(3, 5), Point(3.5, 4))
leg_two.draw(win)

arm_one = Line(Point(3, 6.5), Point(3.5, 6))
arm_one.draw(win)

arm_two = Line(Point(3, 6.5), Point(2.5, 6))
arm_two.draw(win)

win.getMouse()