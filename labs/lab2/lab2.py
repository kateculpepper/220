"""
Name: <Kate Culpepper>
<Lab1>.py

Problem: <This program calculates the root-mean-square, harmonic mean and the geometric mean, from input from the user >

Certification of Authenticity:

I certify that this assignment is my own work <Kate Culpepper>
"""
def means():

    user_range = eval(input("Enter the number of values to be entered: "))

    rms_acc = 0
    harmonic_mean_acc = 0
    geometric_mean_acc = 1

    for i in range(user_range):
        values = eval(input("Enter value:"))
        square_values = values ** 2
        rms_acc = rms_acc + square_values
        harmonic_mean_acc = harmonic_mean_acc + 1/values
        geometric_mean_acc = geometric_mean_acc * values

    rms = (rms_acc/user_range) ** .5
    print("The root mean square is :", rms)

    hm = (user_range/harmonic_mean_acc)
    print("The Harmonic mean is:", hm)

    gm = (geometric_mean_acc ** (1/user_range))
    print("The geometric mean is:", gm)


means()
