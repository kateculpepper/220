from math import *


class Sphere:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def surface_area(self):
        surf_a = 4 * pi * (self.radius ** 2)
        return surf_a

    def volume(self):
        sphere_volume = (4/3) * pi * (self.radius ** 3)
        return sphere_volume
