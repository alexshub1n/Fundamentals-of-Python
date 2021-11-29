with open('lesson_5_ex_2_text.txt') as file:
    file_str = file.readlines()
    s = 0
    w = 0
    for i in file_str:
        content = i.split()
        w += len(content)
        s += 1
        print(f'String #{s}: {len(content)} words')
    print(f'Strings = {s}, Words = {w}')
