user_number = int(input('Enter number greater then 0: '))
if user_number <= 0:
    print('Number is not greater then 0!')
else:
    user_number_2 = int(str(user_number)*2)
    user_number_3 = int(str(user_number)*3)
    res_sum = user_number + user_number_2 + user_number_3
    print(res_sum)
