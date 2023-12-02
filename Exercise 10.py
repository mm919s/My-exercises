a = int(input('Please enter the coefficient "a" of the quadratic equation = '))
b = int(input('Please enter the coefficient "b" of the quadratic equation = '))
c = int(input('Please enter the coefficient "c" of the quadratic equation = '))
import math
delta = ((b ** 2) - (4 * a * c))
root_delta = math.sqrt(delta)
x1 = (-b + root_delta) / (2 * a)
x2 = (-b - root_delta) / (2 * a)
print('x1 = ', x1, ',', 'x2 = ', x2)
#Write a program that calculates the roots (answers) of a quadratic equation