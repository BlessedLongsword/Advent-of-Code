# Day 6

# Input

from util.get_input import get_input

def get_area_map():
    return get_input(2024, 6).splitlines()


# Part 1

def find_initial_guard_position_and_direction(area_map):
    for i in range(len(area_map)):
        for j in range(len(area_map[0])):
            if area_map[i][j] == '^':
                return (i, j), 0
            if area_map[i][j] == '>':
                return (i, j), 1
            if area_map[i][j] == 'v':
                return (i, j), 2
            if area_map[i][j] == '<':
                return (i, j), 3
    return 'Where is the guard XD?'

def perform_step(area_map, guard_position, directions, guard_direction, obstacle_positions = set()):
    i, j = guard_position
    di, dj = directions[guard_direction]
    ti, tj = i + di, j + dj
    if not guard_is_within_area(area_map, (ti, tj)):
        return (ti, tj), guard_direction
    elif area_map[ti][tj] == '#' or (ti, tj) in obstacle_positions:
        return guard_position, (guard_direction + 1) % len(directions)
    else:
        return (ti, tj), guard_direction

def guard_is_within_area(area_map, guard_position):
    height = len(area_map)
    width = len(area_map[0])
    i, j = guard_position
    return 0 <= i < height and 0 <= j < width

def count_guard_distinct_positions(area_map, guard_position, directions, guard_direction):
    visited = set()
    visited.add(guard_position)
    while True:
        guard_position, guard_direction = perform_step(area_map, guard_position, directions, guard_direction)
        if guard_is_within_area(area_map, guard_position):
            visited.add(guard_position)
        else:
            break
    return len(visited)

def part1(area_map):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    initial_guard_position, initial_guard_direction = find_initial_guard_position_and_direction(area_map)
    print(f'The guard will visit {count_guard_distinct_positions(area_map, initial_guard_position, directions, initial_guard_direction)} positions before leaving the mapped area.')

part1(get_area_map())


# Part 2

def count_possible_obstructions(area_map, guard_position, directions, guard_direction):
    original_visited = set()
    initial_guard_position, initial_guard_direction = guard_position, guard_direction
    original_visited.add(guard_position)
    while True:
        guard_position, guard_direction = perform_step(area_map, guard_position, directions, guard_direction)
        if guard_is_within_area(area_map, guard_position):
            original_visited.add(guard_position)
        else:
            break

    acc = 0
    for i, position in enumerate(original_visited):
        pi, pj = position
        visited = set()
        guard_position, guard_direction = initial_guard_position, initial_guard_direction
        prev_guard_position, prev_guard_direction = None, None
        visited.add(((guard_position, guard_direction), (prev_guard_position, prev_guard_direction)))
        while True:
            prev_guard_position = guard_position
            guard_position, guard_direction = perform_step(area_map, guard_position, directions, guard_direction, {(pi, pj)})
            if not guard_is_within_area(area_map, guard_position):
                break
            if ((guard_position, guard_direction), (prev_guard_position, prev_guard_direction)) in visited:
                acc += 1
                break
            visited.add(((guard_position, guard_direction), (prev_guard_position, prev_guard_direction)))
    return acc

def part2(area_map):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    initial_guard_position, initial_guard_direction = find_initial_guard_position_and_direction(area_map)
    print(f'There are {count_possible_obstructions(area_map, initial_guard_position, directions, initial_guard_direction)} possible positions for obstruction.')

part2(get_area_map())
