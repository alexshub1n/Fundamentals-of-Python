with open('lesson_5_ex_4_text.txt', 'r') as file, open('lesson_5_ex_4_2_text.txt', 'w', encoding='utf8') as file_2:
    content = file.readlines()
    my_list = []
    my_dict = {}
    ru_dict = {'1': 'Один', '2': 'Два', '3': 'Три', '4': 'Четыре'}
    for i in content:
        dict_line = i.split()
        dict_rec = {dict_line[2]: dict_line[0]}
        my_dict.update(dict_rec)
    my_dict.update(ru_dict)
    for i in my_dict.keys():
        my_list.append(f'{my_dict.get(i)} - {i}\n')
    file_2.writelines(my_list)
