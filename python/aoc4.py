def parse_input_file():
    file = open('input_4.txt', 'r')
    bingo_nums = file.readline().rstrip().split(',')
    bingo_nums = [int(b) for b in bingo_nums]

    matrix_list = []
    curr_matrix = []
    for line in file:
        if line == '\n': 
            # Empty line
            if curr_matrix:
                matrix_list.append([curr_matrix, False])
            curr_matrix = []
        else:
            num_list = line.rstrip().split()
            num_list = [[int(n), False] for n in num_list]
            curr_matrix.append(num_list)
    matrix_list.append([curr_matrix, False])
    return bingo_nums, matrix_list

def mark_matrix(matrix, num):
    for l in matrix:
        for n in l:
            if n[0] == num:
                n[1] = True

def is_bingo(matrix):
    # Horizontal
    allTrue = True
    for l in matrix:
        for n in l:
            allTrue = allTrue and n[1]
        if allTrue:
            return True
        allTrue = True
    
    #Vertical
    allTrue = True
    for j in range(0, 5):
        for i in range(0, 5):
            allTrue = allTrue and matrix[i][j][1]
        if allTrue:
            return True
        allTrue = True
    
    return False

def calc_result(matrix, winning_num):
    sum = 0
    for l in matrix:
        for n in l:
            if not n[1]:
                sum += n[0]
    return sum * winning_num

bingo_nums, matrix_list = parse_input_file()
for num in bingo_nums:
    for matrix in matrix_list:
        if not matrix[1]:
            mark_matrix(matrix[0], num)
            if is_bingo(matrix[0]):
                print("Bingo!")
                matrix[1] = True
                final_res = calc_result(matrix[0], num)
                print(num, final_res)
print(final_res)