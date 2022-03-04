"""
Name: <your name goes here – first and last>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""
from encryption import encode
from encryption import encode_better


def number_words(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "w")

    count = 1
    for line in infile:
        for word in line.split():
            outfile.write(str(count) + " " + word + "\n")
            count = count + 1

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
        outfile.write(employeeName + " {:.2f}".format(weeklyWage) + "\n")

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
        friendfile.write(line)

    file.close()
    friendfile.close()


def send_safe_message(file_name, friend_name, key):
    file = open(file_name, "r")
    friendfile = open(friend_name + ".txt", "w")

    for line in file:
        friendfile.write(encode(line, key) + "\n")

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
    friendfile.write(encode_better(msg, key))

if __name__ == '__main__':
    # number_words("pad.txt", "pad2.txt")
    # hourly_wages("wages.txt", "wages2.txt")
    # calc_check_sum("0-072-94652-0")
    # send_message("friend.txt", "justin")
    # send_safe_message("friend.txt", "justin", 2)
    send_uncrackable_message("friend.txt", "justin", "pad.txt")
