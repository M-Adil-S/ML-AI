#Write a Python program to find the volume of a sphere with diameter 12 cm. Formula: V=4/3 * π * r 3

import math

diameter = 12
radius = diameter / 2

def find_sphere_volume(radius):
    sphere_volume = 4 / 3 * math.pi * (radius ** 3)
    print('Volume of the sphere = {:.3f}'.format(sphere_volume))

find_sphere_volume(radius)

