x = int(input('Please enter a number = '))
if x % 2 == 0:
    event = x
    odd = 0
else:
    odd = x
    even = 0
for i in range(1, 3):
    y = int(input('Please enter a number = '))
    if y % 2 == 0:
        even += y
    else:
        odd += y
if even >= odd:
    max = even
    print('Max (even) = ', even)
else:
    max = odd
    print('Max (odd) = ', odd)
#Write a program that takes 3 numbers from a user and puts even numbers in even variable and odd numbers in odd variable
#and calculates the Max among even and odd variables and prints the amount of Max variable