"""
operators (none of theses change the original list )
<seq> + <seq>              - concatenation
<seq> * <int- expression>  - repetition
<seq>[]                    - indexing
<seq>[:]                   - slicing (always returns a list)
len<seq>                   - length
for <var> in <seq>:        - iteration
<expr> in <seq>            - Membership check
                                - checkis if a value is in the list
                                - returns a boolean

my_list = [3,4,5]
for i in my_list
    print(i)
    >>>3,4,5
for i in range(len(my_list))
    print(i)
    >>>0,1,2

if you watn to add lsitst to gether you have to use conatentations
appendign to a list with multiple thigns will treat it as a new list and a dd a new list within gth list

sort method - you have to tell the sort method how to sort usign  key
requiremnts for the key - the key has to be a function and isnt calle so no ()
                        - they key function has to have one paremeter that is data type related to a list
                        - need to return a number that can be sortd
dictionary {_, _, _}
in a dictionary there are no index values
all the index values are called keys
you can make the key whatever you want
key : value

a tuple is imutable you can't change the teh list

key:value
d = {"jane" : 50, "john": 82)
d["john"]
'>>>>82'

dictionary methods in text book
"""
from graphics import *

def family():
families ={}
families['smith'] = ['sam', 'steve', 'sloan']
a = families['smith']
for key, value in families.items():
    print(key)
    print(value)

def print_c(circles):
    for circle in circles:
        print('({}, {}, {}'.format(circle.getCenter().getX(), circle.getCenter().getX(),
                                   circle.getCenter().getX()), end=" ")


def x_sort(circle):
    return circle.getCenter().getX()


def main():  # (x,y,radius) of a circle
    circle_data = [(20, 30, 90), (2, 3, 909), (25, 35, 9), (208, 33, 990)]
    circle_data.sort(key=sort_data)
    circles= []
    for data in circle_data:
        circles.append(Circle(Point(data[0], data[1]), data[2]))
    " or "
    c1 = Circle(Point(20, 30), 90)
    c2 = Circle(Point(2, 3), 909)
    c3 = Circle(Point(25, 39), 9)
    c4 = Circle(Point(208, 3), 990)
    circles = [c1, c2, c3, c4]
    circles.sort(key=x_sort)
    print_c(circles)
    family()