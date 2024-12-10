# Day 10

# Input

from util.get_input import get_input

def get_topographic_map():
    topographic_map = list()
    for line in get_input(2024, 10).splitlines():
        topographic_map.append([int(height) for height in line])
    return topographic_map

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# Part 1

def get_trailheads(topographic_map):
    trailheads = set()
    for i in range(len(topographic_map)):
        for j in range(len(topographic_map[0])):
            if topographic_map[i][j] == 0:
                trailheads.add((i, j))
    return trailheads

def is_valid_step(topographic_map, position, direction):
    i, j = position
    di, dj = direction
    ti, tj = i + di, j + dj
    height = len(topographic_map)
    width = len(topographic_map[0])
    if not (0 <= ti < height and 0 <= tj < width):
        return False
    if not topographic_map[ti][tj] - topographic_map[i][j] == 1:
        return False
    return True

def trail(topographic_map, position, directions, peaks):
    i, j = position
    if topographic_map[i][j] == 9:
        peaks.add((i, j))
    for direction in directions:
        if is_valid_step(topographic_map, position, direction):
            di, dj = direction
            trail(topographic_map, (i + di, j + dj), directions, peaks)

def get_total_score(topographic_map, directions):
    trailheads = get_trailheads(topographic_map)
    total_score = 0
    for trailhead in trailheads:
        peaks = set()
        trail(topographic_map, trailhead, directions, peaks)
        total_score += len(peaks)
    return total_score

print(f'The sum of the scores of all trailheads in the topographic map is {get_total_score(get_topographic_map(), directions)}.')


# Part 2

def trail2(topographic_map, position, directions):
    i, j = position
    if topographic_map[i][j] == 9:
        return 1
    valid_step_targets = set()
    for direction in directions:
        if is_valid_step(topographic_map, position, direction):
            di, dj = direction
            valid_step_targets.add((i + di, j + dj))
    if len(valid_step_targets) > 0:
        return sum(trail2(topographic_map, step_target, directions) for step_target in valid_step_targets)
    return 0

def get_total_ratings(topographic_map, directions):
    trailheads = get_trailheads(topographic_map)
    total_ratings = 0
    for trailhead in trailheads:  
        total_ratings += trail2(topographic_map, trailhead, directions)
    return total_ratings

print(f'The sum of the ratings of all trailheads in the topographic map is {get_total_ratings(get_topographic_map(), directions)}.')
