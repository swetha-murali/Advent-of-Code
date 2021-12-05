from collections import defaultdict
#point = [[0,0,1,2]]
def calculate_intersection(points_range):
    point_map = defaultdict(int)
    for point in points_range:
        # Veritical Line
        if point[0] == point[2]:
            min_y, max_y = min(point[1], point[3]), max(point[1], point[3])
            for y in range (min_y, max_y+1):
                point_map[(point[0], y)] += 1
        # Horizontal Line
        elif point[1] == point[3]:
            min_x, max_x = min(point[0], point[2]), max(point[0], point[2])
            for x in range (min_x, max_x+1):
                point_map[(x, point[1])] += 1
        else:
            # Diagonal
            dx, dy = point[2]-point[0], point[3]-point[1]
            if dx == dy or dx == -dy:
                start_x, start_y, end_x, end_y = point[0], point[1], point[2], point[3]
                x, y = start_x, start_y
                while True:
                    point_map[(x,y)] += 1
                    if x == end_x and y == end_y:
                        break
                    if x < end_x:
                        x += 1
                    else:
                        x -= 1
                    if y < end_y:
                        y += 1
                    else:
                        y -= 1        
    print(point_map)
    count = 0
    for v in point_map.values():
        if v > 1:
            count += 1
    print(count)

file = open('input_5.txt', 'r')
all_points = []
for line in file:
    points_range = line.split('->')
    points_s = points_range[0].strip()
    points_s = points_s.split(',')
    points_e = points_range[1].strip()
    points_e = points_e.split(',')
    point = [int(points_s[0]), int(points_s[1]), int(points_e[0]), int(points_e[1])]
    all_points.append(point)
calculate_intersection(all_points)
