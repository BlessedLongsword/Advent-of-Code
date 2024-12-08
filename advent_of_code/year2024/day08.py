# Day 8

# Input

from util.get_input import get_input

def get_antenna_map():
    return get_input(2024, 8).splitlines()


# Part 1

def get_antenna_locations(antenna_map):
    antenna_locations = dict()
    height, width = len(antenna_map), len(antenna_map[0])
    for i in range(height):
        for j in range(width):
            antenna = antenna_map[i][j]
            if antenna in antenna_locations:
                antenna_locations[antenna].append((i, j))
            else:
                if antenna != '.':
                    antenna_locations[antenna] = [(i, j)]
    return antenna_locations

def get_distance_between_antennas(antenna1, antenna2):
    return (abs(antenna1[0] - antenna2[0]), abs(antenna1[1] - antenna2[1]))

def is_antinode_in_map(antenna_map, position):
    i, j = position
    height, width = len(antenna_map), len(antenna_map[0])
    return 0 <= i < height and 0 <= j < width

def count_unique_antinode_positions(antenna_map):
    antenna_locations = get_antenna_locations(antenna_map)
    antinode_positions = set()
    for antenna in antenna_locations:
        locations = antenna_locations[antenna]
        for i in range(len(locations)):
            li1, lj1 = locations[i]
            for j in range(i + 1, len(locations)):
                li2, lj2 = locations[j]
                di, dj = get_distance_between_antennas((li1, lj1), (li2, lj2))
                antinode1 = (li1 - di, lj1 + dj * (-1 if lj1 < lj2 else 1))
                antinode2 = (li2 + di, lj2 + dj * (-1 if lj1 > lj2 else 1))
                if is_antinode_in_map(antenna_map, antinode1): antinode_positions.add(antinode1)
                if is_antinode_in_map(antenna_map, antinode2): antinode_positions.add(antinode2)
    return len(antinode_positions)

print(f'{count_unique_antinode_positions(get_antenna_map())} unique locations contain an antinode.')


# Part 2

def count_unique_antinode_positions_with_resonance(antenna_map):
    antenna_locations = get_antenna_locations(antenna_map)
    antinode_positions = set()
    for antenna in antenna_locations:
        locations = antenna_locations[antenna]
        for i in range(len(locations)):
            li1, lj1 = locations[i]
            antinode_positions.add((li1, lj1))
            for j in range(i + 1, len(locations)):
                li2, lj2 = locations[j]
                antinode_positions.add((li2, lj2))
                di, dj = get_distance_between_antennas((li1, lj1), (li2, lj2))
                count1 = 1
                antinode1 = (li1 - di * count1, lj1 + dj * count1 * (-1 if lj1 < lj2 else 1))
                while is_antinode_in_map(antenna_map, antinode1):
                    antinode_positions.add(antinode1)
                    count1 += 1
                    antinode1 = (li1 - di * count1, lj1 + dj * count1 * (-1 if lj1 < lj2 else 1))
                count2 = 1
                antinode2 = (li2 + di * count2, lj2 + dj * count2 * (-1 if lj1 > lj2 else 1))
                while is_antinode_in_map(antenna_map, antinode2):
                    antinode_positions.add(antinode2)
                    count2 += 1
                    antinode2 = (li2 + di * count2, lj2 + dj * count2 * (-1 if lj1 > lj2 else 1))
    return len(antinode_positions)

print(f'Now {count_unique_antinode_positions_with_resonance(get_antenna_map())} unique locations contain an antinode.')
