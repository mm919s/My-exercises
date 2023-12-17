import array
import random
counter = 0
sum_num = 0
a = array.array('i', [])
for i in range(10):
    a.append(random.randint(1, 101))
for j in a:
    for k in range(1, 101):
        if j % k == 0 and k != j:
            sum_num += k
    if sum_num == j:
        counter += 1
        j = str(j)
        print(j + " is a perfect number.")
if counter == 0:
    print("Not available.")
