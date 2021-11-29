def my_func(x, y):
    """
    Raising the number x to the power of y
    :param x: float
    :param y: float
    :return: float
    """
    if y >= 0 or x <= 0 or y % 1 != 0:
        print('x is not real positive number or y is not negative integer')
    else:
        # result = x**y
        result = (1 / x)
        while y < -1:
            result *= (1 / x)
            y += 1
    return result


print(my_func(float(input('Enter real positive number x: ')),
              float(input('Enter negative integer y: '))))
