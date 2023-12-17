import array
import random
array1 = array.array('i', [])
for i in range(10):
    array1.append(random.randint(1, 10))
num = int(input("Please enter a digit =  "))
counter = str(array1.count(num))
print("Your number is repeated " + counter + " times")
