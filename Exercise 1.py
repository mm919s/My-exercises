income = int(input('Please enter your income = '))
if income > 0:
    if income < 2000000:
        tax = int(0)
        net_income = int(income)
    elif 2000000 <= income < 3000000:
        tax = int(income / 50)
        net_income = int(income - tax)
    elif 3000000 <= income < 5000000:
        tax = int(income / 100 * 3)
        net_income = int(income - tax)
    else:
        tax = int(income / 10)
        net_income = int(income - tax)
    print('Tax = ', tax, ' , ', 'Net income = ', net_income)
else:
    print('Error')
