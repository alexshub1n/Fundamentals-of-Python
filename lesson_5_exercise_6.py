with open('lesson_5_ex_6_text.txt', 'r', encoding='utf8') as file:
    file_lines = file.readlines()
    my_dict = {}
    for i in file_lines:
        file_str = i.split()
        lesson = file_str[0][:file_str[0].index(':')]
        hours = 0
        for str in file_str:
            numb = ''
            for i in str:
                if i.isdigit() == True:
                    numb += i
            if numb == '':
                numb = 0
            hours += int(numb)
        lesson_hours = {lesson: hours}
        my_dict.update(lesson_hours)
    print(my_dict)
