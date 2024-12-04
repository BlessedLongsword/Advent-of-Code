# Day 3

# Input

def get_directions(file):
    return open(file).read()


# Part 1

direction_map = {'>': (1, 0), '<': (-1, 0), '^': (0, 1), 'v': (0, -1)}

def get_visited_count(directions):
    visited = {(0, 0)}
    i, j = 0, 0
    for direction in directions:
        di, dj = direction_map[direction]
        i, j = i + di, j + dj
        visited.add((i, j))
    return len(visited)

print(f"{get_visited_count(get_directions("input.txt"))} houses at least receive one present.")


# Part 2

def get_visited_count_turns(directions, num_deliverers):
    visited = {(0, 0)}
    deliverers_positions = [(0, 0)] * num_deliverers
    for i, direction in enumerate(directions):
        deliverer_idx = i % num_deliverers
        i, j = deliverers_positions[deliverer_idx]
        di, dj = direction_map[direction]
        i, j = i + di, j + dj
        visited.add((i, j))
        deliverers_positions[deliverer_idx] = (i, j)
    return len(visited)

print(f"Next year {get_visited_count_turns(get_directions("input.txt"), 2)} houses at least receive one present.")
