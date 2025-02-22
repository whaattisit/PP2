# Task 1

from math import *
print("Task 1: \n")
degree = float(input("Input yo degree: "))
print(f"Yo degree is: {degree}, and yo radians is {degree*pi/180}")

# Task 2

print("Task 2: \n")
from math import * 
height = float(input("Height: "))
base1 = float(input("Base one: "))
base2 = float(input("Base two: "))
print(f"Yo trapezoid's area is {height * ( base1 + base2 ) / 2}")

# Task 3

print("Task 3: \n")
from math import *
n = int(input("Number of sides: "))
l = int(input("Length of a side: "))
apothem = l / (2 * tan (pi / n))
area = int((n * l * apothem) / 2)
print (f"Area of yo regular polygon is: {area}")

# Task 4

print("Task 4: \n")
from math import *
l = float(input("Lenght of base: "))
h = float(input("Height of parallelogram: "))

print("Expected Output: ", l * h)
