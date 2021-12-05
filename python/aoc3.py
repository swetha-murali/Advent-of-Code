import copy

def calculate_count_val(input, pos):
    count_val = [0,0]
    split_dict = {'0':[], '1':[]}
    for val in input:
        if val[pos] == '0':
            count_val[0] += 1
            split_dict['0'].append(val)
        else:
            count_val[1] += 1
            split_dict['1'].append(val)
    return count_val, split_dict


file = open('input_3.txt', 'r')
input_list = []
for line in file:
    input_list.append(line.strip())
input_list_ox = copy.deepcopy(input_list)
input_list_co2 = copy.deepcopy(input_list)
# Oxygen Calculation
for i in range(0,12):
    count_val, split_dict = calculate_count_val(input_list_ox, i)
    if count_val[0] > count_val[1]:
        input_list_ox = split_dict['0']
    else:
        input_list_ox = split_dict['1']
    if len(input_list_ox) == 1:
        break
print(input_list_ox) # 1927
for i in range(0,12):
    count_val, split_dict = calculate_count_val(input_list_co2, i)
    if count_val[1] < count_val[0]:
        input_list_co2 = split_dict['1']
    else:
        input_list_co2 = split_dict['0']
    if len(input_list_co2) == 1:
        break
print(input_list_co2) # 3654
print(1927*3654)