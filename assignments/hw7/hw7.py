"""
Name: <Kate Culpepper>
<hw7>.py

Problem: <This program run several functions. the function number_words opens a file and numbers each word,
hourly_wages takes a file with first and last name they pay and work hours then calculates teh total pay for the week
including a new bonus calc_check_sum calculates the sum of an isbn code, the last function take an encode function
and separate inserted files and outputs coded messages>

Certification of Authenticity:

I certify that this assignment is entirely my own work.

"""
from encryption import encode
from encryption import encode_better


def number_words(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "x")

    count = 1
    for line in infile:
        for word in line.split():
            print((str(count) + " " + word + "\n"), file=outfile)
            count = count + 1
    print("\n", file = outfile)
    infile.close()
    outfile.close()


def hourly_wages(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "w")
    for line in infile:
        employee = line.split()
        employeeName = employee[0] + " " + employee[1]
        hourlyWage = float(employee[2])
        hoursWorked = int(employee[3])
        bonus = hoursWorked * 1.65
        weeklyWage = (hourlyWage * hoursWorked) + bonus
        print((employeeName + " {:.2f}".format(weeklyWage) + "\n"), file=outfile)

    infile.close()
    outfile.close()


def calc_check_sum(isbn):
    isbn = isbn.replace("-", "")
    checksum = 0
    count = len(isbn)
    for num in isbn:
        checksum = checksum + (int(num) * count)
        count = count - 1
    return checksum


def send_message(file_name, friend_name):
    file = open(file_name, "r")
    friendfile = open(friend_name + ".txt", "w")

    for line in file:
        print(line, file=friendfile)

    file.close()
    friendfile.close()


def send_safe_message(file_name, friend_name, key):
    file = open(file_name, "r")
    friendfile = open(friend_name + ".txt", "w")

    for line in file:
        print((encode(line, key) + "\n"), file=friendfile)

    file.close()
    friendfile.close()


def send_uncrackable_message(file_name, friend_name, pad_file_name):
    file = open(file_name, "r")
    padfile = open(pad_file_name, "r")
    friendfile = open(friend_name + ".txt", "w")

    key = padfile.read()
    key = key.split(" ")
    key = key[1]
    msg = file.read()
    print(encode_better(msg, key), file=friendfile)


if __name__ == '__main__':
    # number_words("words.txt", "words2.txt")
    # hourly_wages("wages.txt", "wages2.txt")
    # calc_check_sum("0-072-94652-0")
    # send_message("friend.txt", "justin")
    # send_safe_message("friend.txt", "justin", 2)
    send_uncrackable_message("friend.txt", "justin", "pad.txt")
