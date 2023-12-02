income = int(input('Please enter your icome = '))
if 0 <= income < (10 ** 6):
    print('Net income = ', income)
elif (10 ** 6) <= income <= ((10 ** 6) * 3):
    net_income = ((97 / 100) * income)
    print('Net income = ', net_income)
elif income >= ((10 ** 6) * 3):
    income1 = ((91 / 100) * income)
    income2 = ((93 / 100) * income1)
    net_income = income2
    print('Net income = ', net_income)
#Write a program that that takes an income number from a user and calculates the net income