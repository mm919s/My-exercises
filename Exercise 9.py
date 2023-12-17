import array
import random
counter = 0
a = array.array('i', [])
for i in range(10):
    a.append(random.randint(1, 10))
for j in a:
    if j % 2 == 0:
        counter += 1
print(counter)
