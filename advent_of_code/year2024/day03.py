# Day 3

# Input

from util.get_input import get_input

def get_memory():
    return get_input(2024, 3) 


# Part 1

import re

def perform_multiplications(memory):
    pattern = r'mul\(\d{1,3},\d{1,3}\)'
    multiplications = re.findall(pattern, memory)
    return sum(map(lambda mul: int(mul[4:mul.index(',')]) * int(mul[mul.index(',') + 1:-1]), multiplications))

print(f'Adding up all the results of the multiplications gets us {perform_multiplications(get_memory())}.')


# Part 2

def perform_conditional_multiplications(memory):
    pattern = r"(mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))"
    operations = re.findall(pattern, memory)
    enabled = True
    acc = 0
    for operation in operations:
        if re.match(r'mul\(\d{1,3},\d{1,3}\)', operation) and enabled:
            comma = operation.index(',')
            acc += int(operation[4:comma]) * int(operation[comma + 1:-1])
        elif re.match(r'do\(\)', operation):
            enabled = True
        else:
            enabled = False
    return acc

print(f'Adding up all the results of only the enabled multiplications gets us {perform_conditional_multiplications(get_memory())}.')
