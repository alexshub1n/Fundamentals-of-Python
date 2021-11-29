import json
with open('lesson_5_ex_7_text.txt', 'r') as file, open('lesson_5_ex_7_json.json', 'w') as file_j:
    content = file.readlines()
    sum_profit = 0
    n = 0
    dict_profit = {}
    for i in content:
        file_str = i.split()
        profit = int(file_str[2]) - int(file_str[3])
        dist_rec = {file_str[0]: profit}
        dict_profit.update(dist_rec)
        print(f'{file_str[0]} profit: {profit}')
        if profit >= 0:
            sum_profit += profit
            n += 1
    avg_profit = round(sum_profit / n)
    dict_avg = {'average_profit': avg_profit}
    list_result = [dict_profit, dict_avg]
    print(f'Average profit: {avg_profit}')
    print(list_result)
    json.dump(list_result, file_j)


