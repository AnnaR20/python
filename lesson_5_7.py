# 7
import json

with open('lesson_5_7_text.txt') as f:
    fin_res = [int(line.split()[2]) - int(line.split()[3]) for line in f.readlines()]
    f.seek(0)
    names = [line.split()[0] for line in f.readlines()]
    positive_res = [el for el in fin_res if el > 0]
    my_sum = 0
    for el in positive_res:
        my_sum += int(el)
    avg_profit = my_sum/len(positive_res)
    final_list = [dict(zip(names, fin_res)), {'average_profit': avg_profit}]


with open('lesson_5_7_json.json', 'w') as f_json:
    json.dump(final_list, f_json)



