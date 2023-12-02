num1, num2, num3 = input('Please enter 3 numbers separated by "," = ').split(',')
num1a = int(num1)
num2a = int(num2)
num3a = int(num3)
nums = [num1a, num2a, num3a]
nums.sort(reverse=True)
print('The second largest number = ', nums[1])
