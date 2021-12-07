def find_align(crab_positions):
    minimum, maximum = min(crab_positions), max(crab_positions)
    pos_val = float("inf")
    for pos in range(minimum, maximum+1):
        dist = 0
        for crab in crab_positions:
            diff = abs(crab-pos)
            # Binomial coefficient
            dist += diff*(diff+1)/2
        if dist < pos_val:
            pos_val = dist
    print(pos_val)

crabs = open('input_7.txt', 'r').readline().split(',')
crabs = [int(c) for c in crabs]
find_align(crabs)