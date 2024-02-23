"""
--- Day 6: Probably a Fire Hazard ---

Because your neighbors keep defeating you in the holiday house decorating contest year after year, 
you've decided to deploy one million lights in a 1000x1000 grid.

Furthermore, because you've been especially nice this year, Santa has mailed you instructions on 
how to display the ideal lighting configuration.

Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at 
0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle various 
inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, 
inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. 
The lights all start turned off.

To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent you in order.

For example:

    turn on 0,0 through 999,999 would turn on (or leave on) every light.
    toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
    turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.

After following the instructions, how many lights are lit?
"""

import re, numpy as np

def get_instructions(file):
    instructions = []
    for instruction in open(file).read().splitlines():
        operation, unparsed_range = re.split(r'(\bturn off\b|\bturn on\b|\btoggle\b)', instruction)[1:]
        parsed_range = unparsed_range[1:].split(' through ')
        idx1, idx2 = tuple(map(int, parsed_range[0].split(','))), tuple(map(int, parsed_range[1].split(',')))
        instructions.append((operation, idx1, idx2))
    return instructions

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

"""
--- Part Two ---

You just finish implementing your winning light pattern when you realize you mistranslated 
Santa's message from Ancient Nordic Elvish.

The light grid you bought actually has individual brightness controls; each light can have a 
brightness of zero or more. The lights all start at zero.

The phrase turn on actually means that you should increase the brightness of those lights by 1.

The phrase turn off actually means that you should decrease the brightness of those lights by 1, to a minimum of zero.

The phrase toggle actually means that you should increase the brightness of those lights by 2.

What is the total brightness of all lights combined after following Santa's instructions?

For example:

    turn on 0,0 through 0,0 would increase the total brightness by 1.
    toggle 0,0 through 999,999 would increase the total brightness by 2000000.


"""

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