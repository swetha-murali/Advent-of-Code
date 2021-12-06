from collections import defaultdict
from copy import deepcopy

def calc_total_fishies(fishies, days):
    fish_span = defaultdict(int)
    temp_dict = defaultdict(int)
    for f in fishies:
        fish_span[f] += 1
    for _ in range(1, days+1):
        temp_dict.clear()
        to_add = 0
        for j in range(0,9):
            if j not in fish_span:
                continue
            if j == 0:
                temp_dict[6] += fish_span[0]
                to_add = fish_span[0]
            else:
                temp_dict[j-1] += fish_span[j]
        temp_dict[8] = to_add
        fish_span = deepcopy(temp_dict)
    print(fish_span)
    print(sum(fish_span.values()))


file = open('input_6.txt', 'r')
fishies = file.readline().rstrip().split(',')
fishies = [int(f) for f in fishies]
calc_total_fishies(fishies, 80)
calc_total_fishies(fishies, 256)