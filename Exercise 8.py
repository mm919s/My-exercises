x = int(input('Please a number = '))
max = x
min = x
a = 1
b = 0
for i in range(1, 3):
    y = int(input('Please enter a number = '))
    a = a * y
    if y >= max:
        max = x
    elif y <= min:
        min = y
print('Min = ', min, ',', 'Max = ', max)
if (max + min) % 2 == 0:
    if max % 2 != 0:
        a = a * x
        print('Product of 3 input numbers = ', a)
    elif min % 2 != 0:
        print('Min = ', min)
    else:
        for i in range(1, 3):
            b += y
        b += x
        print('Sum of 3 input numbers = ', b)
else:
    if max % 2 == 0:
        print('Max = ', max)
    elif min % 2 == 0:
        print('Max to the power of 2 = ', max ** 2)
    else:
        for i in range(1, 3):
            b += y
        b += x
        print('Sum of 3 input numbers = ', b)
#Write a program that takess 3 numbers from a user and defines Max & Min