num = int(input('Please enter a number = '))
p = 1
q = 0
if num % 2 != 0:
    num = int((num - 1) / 2)
    print('1 ', end=', ')
    for i in range(1, num + 1):
        q += p
        p += q
        print(q, ',', p, end=' , ')
else:
    num = int(num / 2)
    for i in range(num):
        p += q
        q += p
        print(p, ',', q, end=' , ')
# Write a program that takes 3 numbers from user and ...
