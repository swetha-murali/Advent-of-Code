def count_increase(input):
    if not input:
        return 0
    increase_count = 0
    for i in range (0, len(input)-1):
        if input[i+1] > input[i]:
            increase_count += 1
    return increase_count

def three_sum(input):
    if len(input) < 3:
        return 0
    count_increase = 0
    i = 0
    prev_sum = sum(input[i:i+3])
    for i in range (1, len(input)-2):
        # print(input[i:i+3])
        next_sum = sum(input[i:i+3])
        if next_sum > prev_sum:
            count_increase += 1
        prev_sum = next_sum
    return count_increase

file = open('input_1.txt', 'r')
input = []
for line in file:
    input.append(int(line))
# print(input)
print(count_increase(input))
print(three_sum(input))
