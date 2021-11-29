user_input = input('Enter numbers separated by space: ')
my_list = user_input.split()
result_list = []
for i in my_list:
    if my_list.count(i) == 1:
        result_list.append(i)
print(result_list)
