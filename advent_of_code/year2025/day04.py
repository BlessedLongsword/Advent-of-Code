# Day 04

# Input

from util.get_input import get_input

def get_field():
    return [list(line) for line in get_input(2025, 4).splitlines()]

# Part 1

DIRECTIONS = {(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)}

def roll_is_accessible(field, roll_position, max_adjacent_rolls, roll_symbol):
    i, j = roll_position
    lbi, lbj = 0, 0
    ubi, ubj = len(field) - 1, len(field[0]) - 1
    adjacent_rolls_count = 0
    for di, dj in DIRECTIONS:
        ti, tj = i + di, j + dj
        if lbi <= ti <= ubi and lbj <= tj <= ubj:
            adjacent_rolls_count += 1 if field[ti][tj] == roll_symbol else 0;
    return adjacent_rolls_count < max_adjacent_rolls

def count_accessible_rolls(field, max_adjacent_rolls, roll_symbol):
    accessible_rolls_count = 0
    for i in range(len(field)):
        for j in range(len(field[i])):
            accessible_rolls_count += int(roll_is_accessible(field, (i, j), max_adjacent_rolls, roll_symbol)) if field[i][j] == roll_symbol else 0
    return accessible_rolls_count

print(f'A total of {count_accessible_rolls(get_field(), 4, '@')} rolls of paper can be accessed by a forklift.')

# Part 2

def count_removable_rolls(field, max_adjacent_rolls, roll_symbol, void_symbol):
    accessible_rolls_count = 0
    current_accessible_rolls = -1
    while current_accessible_rolls != 0:
        current_accessible_rolls = 0
        for i in range(len(field)):
            for j in range(len(field[i])):
                if roll_is_accessible(field, (i, j), max_adjacent_rolls, roll_symbol) and field[i][j] == roll_symbol:
                    current_accessible_rolls += 1
                    field[i][j] = void_symbol
        accessible_rolls_count += current_accessible_rolls
    return accessible_rolls_count

print(f'A total of {count_removable_rolls(get_field(), 4, '@', '.')} rolls of paper can be removed by a forklift.')
