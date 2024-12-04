# Day 8

# Input

def get_strings(file):
    return open(file).read().splitlines()


# Part 1

def count_chars(strings):
    literals = 0
    characters = 0
    prev = None
    for string in strings:
        characters -= 2
        for char in string:
            if char == '\\':
                characters += prev == '\\'
            else:
                if prev == '\\' and char == 'x':
                    characters -= 2
                characters += 1
            literals += 1
            prev = char if not (prev == '\\' and char == '\\') else None
    return literals - characters

print("The final value for the strings is", count_chars(get_strings("input.txt")))


# Part 2

def count_chars_part2(strings):
    literals = 0
    characters = 0
    for string in strings:
        characters += 2
        for char in string:
            characters += 2 if char == '\\' or char == '"' else 1
            literals += 1
    return characters - literals

print("The new final value for the strings is", count_chars_part2(get_strings("input.txt")))
