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


def main():
from Die import Die
    p = Point(2,3)
    number_of_sides = eval(input('how many sides?: '))
    d = Die(number_of_sides)
    playing = True
    while playing:
        d.roll()
        print(d.get_value())

        stopping = input('hit input to enter:')
        playing = not stopping


if __name__ == '__main__':
    main()
