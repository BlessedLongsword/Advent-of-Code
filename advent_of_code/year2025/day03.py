# Day 03

# Input

from util.get_input import get_input

def get_banks():
    return [list(map(int, list(line))) for line in get_input(2025, 3).splitlines()]

# Part 1

def get_section_joltage(bank, start, stop=None):
    max_rating = 0
    section = bank[start:] if stop is None else bank[start:stop]
    idx = start
    mr_idx = idx
    for rating in section:
        if rating > max_rating:
            max_rating = rating
            mr_idx = idx
        idx += 1
    return max_rating, mr_idx + 1

def get_bank_joltage(bank, battery_count):
    ratings = []
    start, stop = 0, len(bank) - battery_count + 1
    for _ in range(battery_count):
        rating, start = get_section_joltage(bank, start, stop)
        stop += 1
        ratings.append(rating)
    return int(''.join(map(str, ratings)))

print(f'The total output joltage is {sum(get_bank_joltage(bank, 2) for bank in get_banks())}')

# Part 2

print(f'The total output joltage is {sum(get_bank_joltage(bank, 12) for bank in get_banks())}')
