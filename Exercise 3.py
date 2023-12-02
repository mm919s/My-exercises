num1 = int(input('Please enter a 4 digit number = '))
num2 = int(num1 // 1000) #Thousands digit
num3 = int((num1 // 100) % 10) #Hundreds digit
num4 = int((num1 % 100) // 10) #Tens digit
num5 = int(num1 % 10) #Ones digit
if 1 <= num2 <= 9:
    if num5 % 2 == 0 and num3 % 2 == 0:
        print('Your number = ', num1)
    elif num5 % 2 == 0 and num3 % 2 != 0:
        num6 = num5 + num4
        print('Tens digit + Ones digit = ', num6)
    elif num5 % 2 != 0 and num3 % 2 == 0:
        if num5 <= num3:
            min = num5
        else:
            min = num3
        print('Min (Among Hundreds digit and ones digit) = ', min)
    elif num5 % 2 != 0 and num3 % 2 != 0:
        if num4 % 2 == 0:
            print('Tens digit = ', num4)
        else:
            print('Error!')
#Write a program that takes a 4-digit number from the user and ...