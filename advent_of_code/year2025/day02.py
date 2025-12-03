# Day 02

# Input

from itertools import groupby
from util.get_input import get_input

def get_ranges():
    return list(map(lambda x: tuple(map(int, x.split('-'))), get_input(2025, 2).splitlines()[0].split(',')))


# Part 1

def is_invalid_id(id):
    id = str(id)
    if len(id) % 2 != 0:
        return False
    mid = len(id) // 2
    return id[:mid] == id[mid:]

print(f'If you add up all of the invalid ids you get {sum(sum(id for id in range(start, end + 1) if is_invalid_id(id)) for start, end in get_ranges())}')


# Part 2

def all_equal(iterable):
    g = groupby(iterable)
    return next(g, True) and not next(g, False)

def get_interval_widths(id):
    for i in range(1, len(id) // 2 + 1):
        if len(id) % i == 0:
            yield i

def is_invalid_id2(id):
    id = str(id)
    for width in get_interval_widths(id):
        if all_equal(id[i:i+width] for i in range(0, len(id), width)):
            return True
    return False

print(f'If you add up all of the invalid ids you get {sum(sum(id for id in range(start, end + 1) if is_invalid_id2(id)) for start, end in get_ranges())}')
