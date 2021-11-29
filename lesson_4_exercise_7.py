def my_func(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
        yield f


num = int(input('Enter number: '))

for el in my_func(num):
    print(el)
