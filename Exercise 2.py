num1, num2, num3, num4 = input('Please enter 4 numbers separated by "," = ').split(',')
num1a = int(num1)
num2a = int(num2)
num3a = int(num3)
num4a = int(num4)
nums = [num1a, num2a, num3a, num4a]
nums.sort(reverse=True)
if nums[0] % 2 == 0:
    x = nums[-1] * 2
    print('2 times Min = ', x)
else:
    x = nums[0] ** 3
    print('Max to the power of 3 = ', x)
