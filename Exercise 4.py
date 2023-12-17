import array
nums = array.array('i', [])
n = int(input("How many numbers do you want to enter? "))
while type(n) is not int:
    print("Wrong entry data type!")
    n = int(input("Try again with the valid entry data type = "))
counter = 0
for i in range(1, n + 1):
    counter += 1
    if i == 1:
        num = int(input("Please enter the 1st number = "))
        if num == 0:
            break
        nums.append(num)
    elif i == 2:
        num = int(input("Please enter the 2nd number = "))
        if num == 0:
            break
        nums.append(num)
    elif i == 3:
        num = int(input("Please enter the 3rd number = "))
        if num == 0:
            break
        nums.append(num)
    else:
        i = str(i)
        m = "Please enter the " + i + "th number"
        print(m, end=' ')
        num = int(input("= "))
        if num == 0:
            break
        nums.append(num)
        i = int(i)
max_num = max(nums)
for j in nums:
    if j < 50:
        max_num = j
