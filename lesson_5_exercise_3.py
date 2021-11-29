# with open('lesson_5_ex_3_text.txt', 'w') as file:
#     emp_list = ('Smith 20000\nJohnson 10000\nWilliams 15000\nJones 25000\nBrown 30000\nDavis 21000\nMiller '
#                 '27000\nWilson 18000\nMoore 31000\nTaylor 24000')
#     file.writelines(emp_list)

with open('lesson_5_ex_3_text.txt', 'r') as file:
    content = file.readlines()
    low_payment = []
    all_salary = []
    x = 1
    for i in content:
        line = i.split()
        if x <= len(content) and int(line[1]) < 20000:
            low_payment.append(line[0])
            all_salary.append(int(line[1]))
            x += 1
        else:
            all_salary.append(int(line[1]))
            x += 1
    avg_salary = sum(all_salary)/len(all_salary)
print(f'Employee with a salary of less than 20 thousand: {low_payment}')
print(f'Average employee income: {avg_salary}')
