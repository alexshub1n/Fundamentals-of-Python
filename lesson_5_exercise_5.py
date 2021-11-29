with open('lesson_5_ex_5_text.txt', 'w') as file:
    user_input = input('Enter numbers separated by space: ')
    file.write(user_input)
with open('lesson_5_ex_5_text.txt', 'r') as file_2:
    file_str = file_2.read()
    list_str = file_str.split()
    list_int = []
    for i in list_str:
        list_int.append(int(i))
    result = sum(list_int)
    print(result)
