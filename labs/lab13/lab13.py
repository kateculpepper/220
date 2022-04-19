"""
Name: <Kate Culpepper>
<lab 13>.py

Problem: <This assignment runs a program with a series of different functions>

Certification of Authenticity:

I certify that this assignment is my own work>
"""

def star_find(filename):
    open_file = open(filename, 'r')
    line = open_file.readline()
    num_split = line.split(" ")
    star_count = 0
    signals = 0
    for number in num_split:
        signals += 1
        if 4000 <= int(number) <= 5000:
            star_count += 1
            print("magnitude of signal found: ", number)
    print("number of strong pulses:", star_count)
    print("signals checked:", signals)
    open_file.close()




if __name__ == '__main__':
    star_find('signals.txt')
