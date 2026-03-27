
#---------------------- MATH SPECIAL METHODS----------------------#

"""Similar to __getitem__() and __len__(), there are several mathematical special methods that allow us
    to perform built in operations on our custom classes."""

import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self): # returns a string representation w/ print() rather something like "<Vector object ...>"
        return f"Vector({self.x}, {self.y})" # Good practice to make identical to instance creation syntax if possible

    def __abs__(self): # allows us to use math's abs() to see absolute value
        return math.hypot(self.x, self.y)

    def __bool__(self): # allows us to use bool() to make our obj truthy or falsy, in this case returning False if
        return bool(abs(self)) # vector is 0. Must return a bool.

    def __add__(self, other): # allows us to use the + operator for Vector addition
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, other): # allows us to use the * operator for multiplication
        return Vector(self.x * other, self.y * other)


v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = Vector(0, 0)

print(f"Printing vector with print: {v1}")

print(f"Printing abs value of v2: {abs(v2)}")

print(f"Here is a truthy Vector, v2: {bool(v2)}. Here is a falsey, v3: {bool(v3)}")

print(f"Addition, v1 + v2: {v1+v2}")

print(f"Multiplication v1 x3: {v1*3}")


# ------ Additional Notes ------
"""
- Python applies bool(variable) to determine if an object is truthy or falsy, returning the concomitant boolean.
    Objects by default run truthy, unless otherwise specified by the __bool__ dunder method.
    If no bool dunder method is present, python will run .__len__(object) and return False if len is 0. True
    is returned otherwise.
"""