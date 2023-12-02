num1 = int(input('Please enter your 1st number = '))
num2 = int(input('Please enter your 2nd number = '))
if num1 >= num2:
    max = num1
    min = num2
else:
    max = num2
    min = num1
if max > 100:
    if max % 2 == 0:
        print('Max = ')
    else:
        print('Error!')
    print('Max = ', max)
elif 50 < max < 100:
    if max % 2 == 0:
        print('3 times Max = ', 3 * max)
    else:
        print('Error!')
else:
    if min % 2 == 0:
        print('Min = ', min)
#Write a program that takes 2 numbers from a user and highlights the Max & Min and ...