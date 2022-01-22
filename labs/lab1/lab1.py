"""
Name: <Kate Culpepper>
<Lab1>.py

Problem: <This program calculates the monthly interest charge >

Certification of Authenticity:

I certify that this assignment is my own work, but I discussed it with: <Kate Culpepper>
"""
def interest_rate():
    annual = eval(input("What is your annual interest rate? "))
    days = eval(input("How many days are in your billing cycle? "))
    netbalance = eval(input("What is your previous net balance? "))
    payment = eval(input("what was your payment amount? "))
    payday = eval(input("What day did you make your payment? "))

    step1 = netbalance * days
    step2 = payment * (days - payday)
    step3 = step1 - step2
    step4 = step3 / days
    step5 = annual / 12
    step6 = step4 * (step5 / 100)

    print("Your monthly interest charge is ", step6)


if __name__ == '__main__':
    interest_rate()
