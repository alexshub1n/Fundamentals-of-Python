user_number = int(input('Enter integer number greater then 0: '))
if user_number <= 0:
    print('Number is not greater then 0!')
else:
    max_number = 0
    while user_number > 0:
        if user_number % 10 > max_number:
            max_number = user_number % 10
            user_number //= 10
        else:
            user_number //= 10
    print(max_number)
