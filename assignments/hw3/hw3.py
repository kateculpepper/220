"""
Name: <your name goes here – first and last>
<ProgramName>.py

Problem: <In this program it runs functions that output, the average grade, totals tips,
 computes the square root, outputs a sequence, and outputs approximation of pi >

Certification of Authenticity:

I certify that this assignment is entirely my own work.

"""


def average():
    grades = eval(input("How many grades will you enter ?: "))
    grade_acc = 0
    for i in range(grades):
        num_grade = eval(input("Enter grade: "))
        grade_acc = grade_acc + num_grade

    avg_grade = grade_acc / grades
    print("The average grade is:", avg_grade)


def tip_jar():
    tip_acc = 0
    for i in range(5):
        tip = eval(input("How much would you like to tip?: "))
        tip_acc = tip_acc + tip
    print("total tips:", tip_acc)


def newton():
    sqrt_num = eval(input("What number do you want to square root?:"))
    num_calc = eval(input("How many times should we improve the approximation?:"))
    approx = sqrt_num
    for i in range(num_calc):
        approx = (approx + (sqrt_num / approx)) / 2
    print("The square root is approximately:", approx)


def sequence():
    terms = eval(input("How many terms would you like?: "))

    for i in range(1, terms, 2):
        print(i)
        for j in range(1, 2):
            print(i)


def pi():
    pi_terms = eval(input("How many terms in the series?"))
    approx = 1
    for i in range(2, pi_terms + 1, 2):
        for j in range(i):
            approx = approx * (i / (i - 1)) * (i / (i + 1))

    print(approx*2)


if __name__ == '__main__':
    # average()
    # tip_jar()
    # newton()
    #sequence()
    #pi()
