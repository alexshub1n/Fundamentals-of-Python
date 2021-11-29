def get_numbers(num_1, num_2):
    """
    Dividing the first number by the second
    :param num_1: int, float
    :param num_2: int, float
    :return: float
    """

    if num_2 == 0:
        division_numbers = ("'Second number can't be equal zero'")
    else:
        division_numbers = num_1 / num_2
    return division_numbers


print(get_numbers(float(input('Enter first number: ')),
                  float(input('Enter second number: '))))
