# Day 05

# Input

from util.get_input import get_input

def get_database():
    ranges = []
    ids = []
    for line in get_input(2025, 5).splitlines():
        if '-' in line:
            ranges.append(tuple(map(int, line.split('-'))))
        elif len(line) == 0:
            continue
        else:
            ids.append(int(line))
    return ranges, ids


# Part 1

def item_is_fresh(id, ranges):
    for lb, ub in ranges:
        if lb <= id <= ub:
            return True
    return False

def get_fresh_items(database):
    ranges, ids = database
    fresh_count = 0
    for id in ids:
        fresh_count += 1 if item_is_fresh(id, ranges) else 0
    return fresh_count

print(f'{get_fresh_items(get_database())} items are fresh.')

# Part 2

def merge_ranges(ranges):
    ranges = sorted(ranges)
    merged_ranges = set()
    lb, ub = ranges[0]
    for tlb, tub in ranges[1:]:
        if tlb <= ub:
            ub = tub if tub > ub else ub
        else:
            merged_ranges.add((lb, ub))
            lb, ub = tlb, tub
    merged_ranges.add((lb, ub))
    return merged_ranges


def get_all_fresh_items(database):
    ranges, _ = database
    fresh_count = 0
    for lb, ub in merge_ranges(ranges):
        fresh_count += ub - lb + 1
    return fresh_count

print(f'A total of {get_all_fresh_items(get_database())} items are fresh.')
