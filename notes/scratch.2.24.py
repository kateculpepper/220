from graphics import *


def change_point(p, x, y):
    p.move(x, y)


my_point = Point(2, 3)
my_same_point = my_point
change_point(my_point, 100, 200)
print(my_point.getX(), my_point.getY())
print(my_same_point.getX(), my_same_point.getY())


def double_list(list_one):
    for index in range(len(list_one)):
        list_one[index] = list_one[index] * 2


my_list = [1, 2, 3, 4, 5]
my_same_list = my_list
print(my_list)
double_list(my_list)
print(my_list)

# chapter 7 control structures

# a for loop is a type of control structure, alters the flow of the program
# functions can be considered a control structure, also interrupt the linear flow
# decision structure - allows your program to execute different statement depending on
   # some conditions

   if <condition> : #will only run if the the statement is true
       <body>:
