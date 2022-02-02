"""
Name: <Kate Culpepper>
<Lab1>.py

Problem: <This program ouputs the avg number of vehicles per day, total of vehicles on all roads,
 and the average number of vehicles per road, using input from the user >

Certification of Authenticity:

I certify that this assignment is my own work <Kate Culpepper>
"""


def traffic():
    roads = eval(input("How many roads were surveyed?:"))

    acc_total_vehicle = 0

    for i in range(roads):
        vehicle_per_day = 0
        print("How many days was road", i + 1, "surveyed?:")
        days = eval(input(""))

        for j in range(days):
            print("How many cars travelled on day", j + 1, "?:")
            cars = eval(input(""))
            acc_total_vehicle = acc_total_vehicle + cars
            vehicle_per_day = vehicle_per_day + cars
            car_avg = vehicle_per_day / days

        print("average vehicles per day:", car_avg)

    print("Total number of vehicles traveled on all roads:", acc_total_vehicle)
    print("Average number of vehicles per road:", acc_total_vehicle / roads)


traffic()
