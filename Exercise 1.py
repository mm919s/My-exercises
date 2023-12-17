num1 = int(input("Please enter the 1st number = "))
counter1 = 2
max_num = num1
min_num = num1
for i in range(1, 3):
    if counter1 == 2:
        num2 = int(input("Please enter the 2nd number = "))
    elif counter1 == 3:
        num2 = int(input("Please enter the 3rd number = "))
    else:
        counter1 = str(counter1)
        print("Please enter the " + counter1 + "th number ", end='')
        num2 = int(input("= "))
        counter1 = int(counter1)
    if num2 >= max_num:
        max_num = num2
    else:
        min_num = num2
    counter1 += 1
if max_num % 2 == 0:
    counter2 = 1
    factorial = 1
    for j in range(1, max_num + 1):
        counter2 += 1
        factorial *= counter2
    print("The factorial of the max num is", factorial)
else:
    if max_num % 5 == 0:
        counter2 = 0
        sum_num = 0
        for k in range(1, max_num + 1):
            counter2 += 1
            sum_num += counter2
        print("The sum of nums from 1 to max num is", sum_num)
    else:
        p = 1
        q = 1
        print("1, 1", end=', ')
        for a in range(3, max_num + 1):
            if a % 2 != 0:
                if a == max_num:
                    p += q
                    print(p)
                else:
                    p += q
                    print(p, end=', ')
            else:
                q += p
                print(q, end=', ')
