import random
num1 = int(input("Please enter a number in range 1 to 6 = "))
num2 = random.randint(1, 7)
if num1 >= num2:
    max_num = num1
else:
    max_num = num2
counter1 = 0
counter2 = 1
for i in range(1, max_num + 1):
    counter1 += 1
    counter2 *= counter1
counter2 = str(counter2)
print(counter2 + " is the factorial of the max number.")
