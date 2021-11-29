with open('lesson_5_ex_1_text.txt', 'a') as file:
    user_str = 'none'
    while user_str != '':
        if user_str == '':
            break
        else:
            user_str = input('Enter text or enter empty line to end: ')
            file.writelines(user_str + '\n')
