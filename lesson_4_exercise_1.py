# (выработка в часах * ставка в час) + премия.
from sys import argv

print(argv)
if len(argv) == 4:
    emp_salary = (int(argv[1]) * int(argv[2])) + int(argv[3])
    print(emp_salary)
else:
    print('Invalid number of arguments')
