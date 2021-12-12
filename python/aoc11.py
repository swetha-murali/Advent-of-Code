from copy import deepcopy

def get_matrix(file):
    matrix = []
    for line in file:
        row = [int(c) for c in line.strip()]
        matrix.append(row)
    return matrix

def increment_matrix(matrix, no_increment):
    r, c = len(matrix), len(matrix[0])
    for i in range(0,r):
        for j in range(0,c):
            if (i,j) not in no_increment:
                matrix[i][j] += 1
    return matrix

def get_9s_indices(matrix):
    index_set = set()
    r, c = len(matrix), len(matrix[0])
    for i in range(0,r):
        for j in range(0,c):
            if matrix[i][j] >= 9:
                index_set.add((i,j))
                matrix[i][j] = 0
    return index_set

def in_range(index, r, c):
    if index[0] < 0 or index[0] >= r:
        return False
    if index[1] < 0 or index[1] >= c:
        return False
    return True

def get_flash_count(matrix):
    r, c = len(matrix), len(matrix[0])
    positions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1,-1), (1, 0), (1,1)]
    index_9s = get_9s_indices(matrix)
    visited = deepcopy(index_9s)
    flash_count = 0
    if index_9s:
        flash_count = len(index_9s)
        while len(index_9s) > 0:
            idx = index_9s.pop()
            for p in positions:
                adj_pos = (idx[0]+p[0], idx[1]+p[1])
                if in_range(adj_pos, r, c) and adj_pos not in visited:
                    matrix[adj_pos[0]][adj_pos[1]] += 1
                    if matrix[adj_pos[0]][adj_pos[1]] >= 9:
                        index_9s.add(adj_pos)
                        visited.add(adj_pos)
                        flash_count += 1
                        matrix[adj_pos[0]][adj_pos[1]] = 0
    # print(flash_count)
    if flash_count == 100:
        return matrix, flash_count
    matrix = increment_matrix(matrix, visited)
    return matrix, flash_count

def part1(matrix):
    total_flash = 0
    for i in range(1,101):
        # print("Step", i)
        matrix, flash_count = get_flash_count(matrix)
        total_flash += flash_count
        # print(matrix)
    print(total_flash)

def part2(matrix):
    i = 0
    while True:
        i += 1
        # print("Step", i)
        matrix, flash_count = get_flash_count(matrix)
        if flash_count == 100:
            break
    print(i)

file = open('input_11.txt', 'r')
matrix = get_matrix(file)
print(matrix)
# part1(matrix)
part2(matrix)