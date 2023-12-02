num1 = int(input('Please enter a number = '))
import math
if num1 < 10:
    if num1 % 2 == 0:
        print('Input num = ', num1)
    else:
        num2 = num1 ** 2
elif 10 < num1 < 100:
    if num1 % 2 ==0:
        print('Input number to the power of 3', num1 ** 3)
    else:
        print(math.sqrt(num1))
else:
    print('Error!')
#Write a program that takes a number from a user and if ...