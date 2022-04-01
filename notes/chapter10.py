""" chapter 10

classes/ objects
class - there to help us organize our data, has data a functionality
that it can do with that data
- divided into two parts what does it have and what does it do

ex, Circle class
has:
- center  - instance variable
-radius   - instance variable

methods:
- .move()
-.getcenter()
-.getradius()

  obj.            constructor
   c    =   <Circle(Point(3,4),10)>

obj. - instance of a class

getter and setters
getter - is going to return the value of an instance variable
setter -

classes will go into seperate file
cars() - the file name should cars.py

ex. class
die.py
first ask waht does it have?
# has sides
#roll
#weight for each side maybe?

class Die:
    #constructors
    def__init__( self, num_sides ):     #self is alwats the first parameter
           <body>

    #methods
go to die.py in notes file to see created die class
"""
# from graphics import *
# from die import Die
from student import Student


def main():
    # d = Die(6)
    # d2 = Die(12)
    # d.roll()
    # d2.roll()
    # print(d.get_value(), d2.get_value())

    student_file = open('student.txt', 'r')
    student_file.readline()
    students = []
    for line in student_file.readlines():
        split_student = line.split(',')
        name = split_student[0]
        hours = split_student[1]
        points = split_student[2]
        student = Student(name, hours, points)
        students.append(student)
    print(students)
    for student in students:
        print(student.get_name())


if __name__ == '__main__':
    main()
