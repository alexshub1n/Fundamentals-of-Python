def user_sum(str_numbers):
    """
    Sum of numbers entered through a space
    :param str_numbers: str
    :return: tuple
    """
    list_str = list(str_numbers.split(' '))
    list_int = []
    for item in list_str:
        if item != 'x':
            list_int.append(int(item))
            x = False
        else:
            x = True
            break
    sum_list = sum(list_int)
    tuple_result = (sum_list, x)
    return tuple_result


stop = False
sum_result = 0
while stop == False:
    tuple_result = user_sum(input('Enter numbers to add, separated by a space: '))
    stop = tuple_result[1]
    sum_result += tuple_result[0]
    print(sum_result)
