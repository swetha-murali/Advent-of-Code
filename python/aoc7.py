def find_align(crab_positions):
    minimum, maximum, pos_val = min(crab_positions), max(crab_positions), float("inf")
    for pos in range(minimum, maximum+1):
        dist = 0
        for crab in crab_positions:
            diff = abs(crab-pos)
            # Binomial coefficient
            dist += diff*(diff+1)/2
        pos_val = min(pos_val, dist)
    print(pos_val)

crabs = list(map(int, open('input_7.txt', 'r').readline().split(',')))
find_align(crabs)