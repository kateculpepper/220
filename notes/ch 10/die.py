from random import randint


class Die:
    def __init__(self, num_sides):  # second parameter is whatever is passed in
        self.sides = num_sides  # we know they are instance variables because fo 'self.' the value stays the same
        self.value = 1

    def get_value(self):
        return self.value

    def roll(self):
        new_value = randint(1, self.sides)
        self.value = new_value



