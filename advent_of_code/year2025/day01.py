# Day 1

# Input

from util.get_input import get_input

ROTATION_MAP = {'L': lambda a, b, c: (a - b) % c, 'R': lambda a, b, c: (a + b) % c}

def get_rotations():
    rotations = list(map(lambda x: (x[0], int(x[1:])), get_input(2025, 1).splitlines()))
    return rotations


# Part 1

def get_password(initial_value, wheel_positions, rotations):
    result = 0
    current_value = initial_value
    for direction, value in rotations:
        current_value = ROTATION_MAP[direction](current_value, value, wheel_positions)
        result += 1 if current_value == 0 else 0
    return result

print(f'The password to open the door is {get_password(50, 100, get_rotations())}')


# Part 2

def get_password_method_0x434C49434B(initial_value, wheel_positions, rotations):
    result = 0
    current_value = initial_value
    for direction, value in rotations:
        previous_value = current_value
        current_value = ROTATION_MAP[direction](current_value, value, wheel_positions)
        traversez_zero_l = direction == 'L' and (current_value > previous_value and previous_value != 0 or current_value == 0 and value % wheel_positions != 0)
        traversed_zero_r = direction == 'R' and current_value < previous_value
        traversed_zero = traversez_zero_l or traversed_zero_r
        result += value // wheel_positions + (1 if traversed_zero else 0)
    return result

print(f'The password to open the door using method 0x434C49434B is {get_password_method_0x434C49434B(50, 100, get_rotations())}')

