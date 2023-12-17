import array
num = int(input("Please enter a number = "))
nums = array.array('i', [])
r = num % 10
nums.append(r)
q = num // 10
while q != 0:
    r = q % 10
    nums.append(r)
    q //= 10
print(nums)
