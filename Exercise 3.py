num = int(input("Please enter a number = "))
digits_sum = 0
while True:
    digit = num % 10
    digits_sum += digit
    num //= 10
    if num == 0:
        break
print("Sum of the digits of this number is", digits_sum)
if digits_sum % 3 == 0:
    print("This number is divisible by 3.")
else:
    print("This number isn't divisible by 3.")
    