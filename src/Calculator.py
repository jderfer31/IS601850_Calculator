import math
from CsvReader import CsvReader


def addition(a, b):
    a = float(a)
    b = float(b)
    c = a + b
    return c

def subtraction(a, b):
    a = float(a)
    b = float(b)
    c = b - a
    return c

def multiplication(a, b):
    a = int(a)
    b = int(b)
    c = a * b
    return c

def division(a, b):
    a = float(a)
    b = float(b)
    c = b / a
    return c

def square(a):
    b = int(a) * int(a)
    return b

def math_squareroot(a):
    b = math.sqrt(a)
    return b

class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def square(self, a):
        self.result = square(a)
        return self.result

    def squareroot(self, a):
        self.result = math_squareroot(a)
        return self.result