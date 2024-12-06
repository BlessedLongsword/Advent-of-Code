# Day 1

# Input

def get_instructions(file):
    return open(file).read()


# Part 1

def fetch_floor(instructions):
    floor = 0
    for instruction in instructions:
        floor += 1 if instruction == '(' else -1
    return floor

print("The instructions take Santa to floor nº", fetch_floor(get_instructions("input.txt")))


# Part 2

def instructions_to_basement_count(instructions):
    floor = 0
    for i, instruction in enumerate(instructions):
        floor += 1 if instruction == '(' else -1
        if floor == -1:
            return i + 1

print("The position of the character that causes Santa to first enter the basement is", instructions_to_basement_count(get_instructions("input.txt")))
