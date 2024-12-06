# Day 6

# Input

import re, numpy as np

def get_instructions(file):
    instructions = []
    for instruction in open(file).read().splitlines():
        operation, unparsed_range = re.split(r'(\bturn off\b|\bturn on\b|\btoggle\b)', instruction)[1:]
        parsed_range = unparsed_range[1:].split(' through ')
        idx1, idx2 = tuple(map(int, parsed_range[0].split(','))), tuple(map(int, parsed_range[1].split(',')))
        instructions.append((operation, idx1, idx2))
    return instructions


# Part 1

def get_lit_lights_count(instructions):
    lights = np.zeros(shape=(1000, 1000), dtype=np.int8)
    for operation, idx1, idx2 in instructions:
        x_start, y_start = idx1
        x_end, y_end = idx2
        if operation == 'turn on':
            lights[x_start:x_end+1, y_start:y_end+1] = 1
        elif operation == 'turn off':
            lights[x_start:x_end+1, y_start:y_end+1] = 0
        else:
            lights[x_start:x_end+1, y_start:y_end+1] += 1
            lights[x_start:x_end+1, y_start:y_end+1] %= 2
    return np.sum(lights)

print(f"There are {get_lit_lights_count(get_instructions("input.txt"))} lit lights.")


# Part 2

def get_total_brightness(instructions):
    lights = np.zeros(shape=(1000, 1000), dtype=np.int8)
    for operation, idx1, idx2 in instructions:
        x_start, y_start = idx1
        x_end, y_end = idx2
        if operation == 'turn on':
            lights[x_start:x_end+1, y_start:y_end+1] += 1
        elif operation == 'turn off':
            lights[x_start:x_end+1, y_start:y_end+1] -= 1
            lights[lights < 0] = 0
        else:
            lights[x_start:x_end+1, y_start:y_end+1] += 2
    return np.sum(lights)

print(f"The total brightness of all lights combined is {get_total_brightness(get_instructions("input.txt"))} after following Santa's instructions.")
