"""
Name: <Kate Culpepper>
<lab 11>.py

Problem: <This assignment runs a program with a series of different functions>

Certification of Authenticity:

I certify that this assignment is my own work>
"""



import random


def find_and_remove_first(list, value):
    i = 0
    while i < len(list):
        i += 1
        if i == value:
            list = list.insert(value, 'kate')
            list.pop(value)


def good_input():
    user_input = eval(input("Enter a number a number between 1 and 10:"))
    while user_input:
        if user_input > 10:
            print(" To high!")
        elif user_input < 1:
            print("too low!")
        else:
            print("number is good!")
        user_input = eval(input("Enter a number a number between 1 and 10:"))


def num_digits():
    n = eval(input("enter a positive integer:"))
    count = 0
    while n != 0:
        divided_num = n // 10
        count += 1
        return divided_num


def hi_lo_game():
    rand_num = random.randint(1, 100)
    while i < range(7):
        guess = int(input("Guess the number:"))
        if guess == rand_num:
            print("correct! you win in ", i + 1, "guesses")
        elif guess > rand_num:
            print("too high!")
        elif guess < rand_num:
            print("too low!")
    else:
        print("you lose. the number was", rand_num)
