"""
Name: <Kate Culpepper>
<HomeWork1>.py

Problem: <This assignment runs a series of different programs that allow you to find
area, volume, shooting percentages for athletes, prices of a coffee sale and a conversion program >

Certification of Authenticity:

I certify that this assignment is my own work, but I discussed it with: <Kate Culpepper>
"""


def calc_rec_area():
    length = eval(input("Enter the Length:"))
    width = eval(input("Enter the width"))
    area = length * width
    print("Area= ", area)


def calc_volume():
    length = eval(input("Enter the length"))
    width = eval(input("Enter the width"))
    height = eval(input("Enter the height"))
    volume = length * width * height
    print("volume =", volume)


def shooting_percentage():
    shots = eval(input("Enter the Player's total shots:"))
    shotsmade = eval(input("Enter how many shots the player made:"))
    percentage = shotsmade / shots * 100
    print("Shooting percentage:", percentage, "%")


def coffee():
    pounds = eval(input("How many pounds of coffee would like?"))
    total = pounds * 11.36 + 1.50
    print("You're total is :", total)


def kilometers_to_miles():
    kilometers = eval(input("How many kilometers did you travel?"))
    miles = kilometers * .62137
    print("That's", miles, "miles!")


if __name__ == '__main__':
    calc_rec_area()
    calc_volume()
    shooting_percentage()
    coffee()
    kilometers_to_miles()
