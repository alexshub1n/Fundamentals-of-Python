def my_func(num_1, num_2, num_3):
    """
    Returning the sum of the two largest numbers of three
    :param num_1: int
    :param num_2: int
    :param num_3: int
    :return: int
    """
    result_sum = num_1 + num_2 + num_3 - min(num_1, num_2, num_3)
    return result_sum


print(my_func(int(input('Enter first number: ')),
              int(input('Enter second number: ')),
              int(input('Enter third number: '))))
