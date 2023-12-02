x = int(input('Please enter a 1 digit number = '))
if -9 <= x <= 9:
    max = x
    min = x
    z = x
    for i in range(1, 3):
        y = int(input('Please enter a 1 digit number = '))
        if -9 <= y <= 9:
            if y >= max:
                max = y
            elif y <= min:
                min = y
    print('Max = ', max)
    if max % 2 == 0:
        for i in range(1, 3):
            z += y
        print('The tens digit of sum of 3 input numbers = ', z // 10)
    else:
        print('Min = ', min)
else:
    print('Invalid number!')
#Write a program that takes 3 of 1 digit numbers and prints Max and if ...