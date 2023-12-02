num1 = int(input('Please enter a number = '))
counter1 = num1
counter2 = num1
for i in range(num1):
    counter1 -= 1
    counter2 += 1
    for j in range(counter1 + 1, counter2):
        if j % 2 == 0 and i % 2 != 0:
            print('*', end='')
        elif j % 2 != 0 and i % 2 == 0:
            print('*', end='')
    print("\n")
# Write a program that takes a number from the user and prints the same number of lines and stars in the middle of-
# the line in each line.
