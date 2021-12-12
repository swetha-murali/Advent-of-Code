from collections import deque, defaultdict

def check_corrupted(line, corrupted_map):
    match = {'}':'{', ']':'[', ')':'(', '>':'<'}
    stack = deque()
    for c in line:
        if c in ['(', '[', '{','<']:
            stack.appendleft(c)
        elif c in [')', ']', '}','>']:
            if not stack or stack[0] != match[c]:
                corrupted_map[c] += 1
                return corrupted_map
            else:
                stack.popleft()
    return corrupted_map

def part1(file):
    corrupted_map = defaultdict(int)
    points = {'}':1197, ']':57, ')':3, '>':25137}
    for line in file:
        corrupted_map = check_corrupted(line.strip(), corrupted_map)
    print(corrupted_map)
    total_score = 0
    for k,v in corrupted_map.items():
        total_score += v * points[k]
    print(total_score)

def is_incomplete(line):
    match = {'}':'{', ']':'[', ')':'(', '>':'<'}
    rev_match = {'{':'}', '[':']', '(':')', '<':'>'}
    stack = deque()
    for c in line:
        if c in ['(', '[', '{','<']:
            stack.appendleft(c)
        elif c in [')', ']', '}','>']:
            if not stack or stack[0] != match[c]:
                return False, None
            else:
                stack.popleft()
    if stack:
        return True, ''.join([rev_match[c] for c in stack])
    return False, None

def calculate_score(line):
    points = {'}':3, ']':2, ')':1, '>':4}
    total_score = 0
    for c in line:
        total_score = (total_score * 5) + points[c]
    return total_score

def part2(file):
    scores = []
    for line in file:
        incomp, output = is_incomplete(line.strip())
        if incomp:
            scores.append(calculate_score(output))
    scores.sort()
    print(scores[len(scores)//2])

file = open('input_10.txt', 'r')
part1(file)
part2(file)