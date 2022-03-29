"""
you can use and to combine of statements
ands come before or's in order of operations in python
and is considered multiplications
addition equates to or
o's equate to false
amd 1's equate to true

x > and
+ > or
0 > false
1 > true

a and false == false

a and true  == a

a or false == a

a or True == true


not not = double negatives will cancel out

boolean algebra
PROPERTIES :

DISTRIBUTIVE PROPERTY :
- a or (b and c ) == (a or b ) and (a or c)
- a and (b or c) == (a and b) or (a and c)

DEMORGAN'S LAW :

not (a or b ) = not a and not b  # if there is an "or" it has to be an and so it swtiches
not(a and b ) == not a or not b

while loops

while true:
continoulsy run until false

break - if youre ina loop it will break out of the loop

truthy/falsey values, they are not booleans values but they are treated as such

0, '', []  = are not false but act like it

score = 0
if score:
    print('nice')
else:
    print('no')
>noooooooo

a string with nothign in it is false

for number 0 is considered false and any other number is considered true

x and y = if x is false reunr x, otherwise, return y.
x or y = if x is true return x other wise return y
not x = if x is false retrun true. otherwise reurn false.

"""


def deMorgan_one(a, b):
    return not (a or b) == (not a and not b)


def deMorgan_test():
    tests = [[True, True], [True, False], [False, False], [False, True]]
    for test in tests:
        a = test[0]
        b = test[1]
        result = deMorgan_one(a, b)
        print('input, {}, output: {}'.format(test, result))


def whoops():
    ans = input('do you want to transfer all of your money ou tof your bank account?')
    if ans == 'y' or ans == 'yes':
        print('ok, transferring..')
    else:
        print('good idea')


def ice_cream():
    ans = input('what is your favorite icecream ? [Vanilla]') or 'vanilla'
    if ans:
        favorite = ans
    else:
        favorite = 'vanilla'
    print('Your favorite is {}'.format(favorite))


def average_while():
    count = eval(input('how many numbers do you have?'))
    acc = 0
    i = 0
    while i < count:
        num = eval(input('enter number:'))
        acc = acc + num
        i = i + 1
    print('average is {}'.format((acc / count)))


def average_interactive():
    acc = 0
    count = 0
    ans = 'y'
    while ans[0] == 'y':
        num = eval(input('enter number :'))
        acc = acc + num
        ans = input('do you want to keep going?')
        count = count + 1
    print('average is {}'.format((acc / count)))


def average_sentinel():
    acc = 0
    count = 0
    num = 0
    while num >= 0:
        acc = acc + num
        count = count + 1
        num = eval(input('enter number (negative to stop):'))
    print('average is {}'.format(acc / (count - 1)))


def average_sentinel_2():
    acc = 0
    count = 0
    num = eval(input('enter number (negative to stop):'))
    while num != '':
        acc = acc + eval(num)
        count = count + 1
        num = eval(input('enter number (enter to stop):'))
    print('average is {}'.format(acc / count))

def average_file():
    acc = 0
    count = 0
    file_name = 'file_data.txt'
    file = open(file_name, 'r')
    for line in file:
        acc = acc + eval(line)
        count = count + 1
    print('average:{}'.format(acc/count))


def average_file_while():
    acc = 0
    count = 0
    file_name = 'file_data.txt'
    file = open(file_name, 'r')
    line = file.readline()
    while line != '':
        acc = acc + eval(line)
        count = count + 1
        line = file.readline()
    print('average:{}'.format(acc/count))


def average_file_nested():
    acc = 0
    count = 0
    file_name = 'file_data.txt'
    file = open(file_name, 'r')
    line = file.readline()
    while line != '':
        nums_string= line.split(',')
        i = 0
        while i < len(nums_string):
            acc = acc + eval(nums_string[i])
            count = count +1
            i = i + 1
        line = file.readline()
    print('average:{}'.format(acc/count))

if __name__ == '__main__':
    # deMorgan_test()
    # whoops()
    # ice_cream()
    # average_while()
    # average_sentinel_2()
    average_file_nested()
