user_input = input('Enter numbers separated by space: ')
my_list = user_input.split()
my_list = [int(i) for i in my_list]

result_list = []
for i in range(len(my_list)):
    if my_list[i] > my_list[i - 1] and i != 0:
        result_list.append(my_list[i])

print(result_list)
