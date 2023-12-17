import array
import random
counter1 = 0
counter2 = 0
a = array.array('i', [])
for i in range(10):
    a.append(random.randint(1, 10))
for j in a:
    for k in range(2, 10):
        if j % k == 0 and j != k:
            break
        else:
            counter1 += 1
    if counter1 == 8:
        counter2 += 1
print(counter2)
