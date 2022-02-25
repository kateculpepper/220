"""
Name: <Kate Culpepper>
<hw6>.py

Problem: <This program runs a series of programs. This program includes a function that converts cash
encodes a message input by the user using a key also input by the user, finds the area and volume of a sphere
finds the sum and cube of the first n natural numbers, and then another function that encodes using a different set
of key and sentence by the user.>

Certification of Authenticity:
I certify that this assignment is entirely my own work.

"""
import math


def cash_converter():
    int_input = eval(input("Enter and integer: "))
    dollar_out = "That is ${}".format(int_input)
    print(dollar_out)


def encode():
    input_msg = input("Enter a message: ")
    input_key = eval(input("enter a key: "))
    output = " "
    for i in range(len(input_msg)):
        msg_value = ord(input_msg[i])
        key_value = input_key
        result_code = (msg_value + key_value)
        output = output + chr(result_code)
    print(output)


def sphere_area(radius):
    res = ((4 * math.pi) * (radius ** 2))
    return float(res)


def sphere_volume(radius):
    res = (((4 / 3) * math.pi) * (radius ** 3))
    return float(res)


def sum_n(number):
    res = (number * (number + 1)) / 2
    return int(res)


def sum_n_cubes(number):
    res = ((number * (number + 1) / 2) ** 2)
    return int(res)


def encode_better():
    input_msg = input("enter a message: ")
    input_key = input("enter a key: ")
    user_code = input_msg
    user_key = input_key
    output = " "
    for i in range(len(user_code)):
        msg_value = ord(user_code[i]) - 65
        key_value = ord(user_key[i % len(user_key)]) - 65
        result_msg = ((msg_value + key_value) % 57) + 65
        output = output + chr(result_msg)
    print(output)


if __name__ == '__main__':
    # cash_converter()
    # encode()
    # res = sphere_area(13)
    # print(res)
    # res = sphere_volume(13)
    # print(res)
    # res = sum_n(100)
    # print(res)
    # res = sum_n_cubes(4)
    # print(res)
    # encode_better()
