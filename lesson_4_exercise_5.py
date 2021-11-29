from functools import reduce as rd


def my_func(prev, curr):
    return prev * curr


my_list = [i for i in range(100, 1001) if i % 2 == 0]
print(rd(my_func, my_list))
