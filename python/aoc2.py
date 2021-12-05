def update_position(curr_pos, command, to_move, aim):
    if command == "forward":
        curr_pos[0] += to_move
        curr_pos[1] += aim*to_move
    elif command == "up":
        aim -= to_move
    elif command == "down":
        aim += to_move
    return curr_pos, aim

file = open('input_2.txt', 'r')
curr_pos = [0,0]
aim = 0
for line in file:
    command, to_move = line.split(" ")
    curr_pos, aim = update_position(curr_pos, command, int(to_move), aim)
print(curr_pos)
print(curr_pos[0]*curr_pos[1])