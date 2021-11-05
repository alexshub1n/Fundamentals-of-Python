revenue = float(input('Enter revenue: '))
cost = float(input('Enter cost: '))
profit = revenue - cost


if revenue > cost:
    print('Profit')
    print('Profitability: ' + str(profit/revenue))
    q_emp = int(input('Enter the number of employees: '))
    print('Profit per employee: ' + str(profit/q_emp))
elif revenue == cost:
    print('Payback')
else:
    print('Loss')
