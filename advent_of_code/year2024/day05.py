# Day 5

# Input

from util.get_input import get_input

ordering_rules = set()
updates = list()
first_section = True
for line in get_input(2024, 5).splitlines():
    if first_section:
        if not line:
            first_section = False
            continue
        ordering_rules.add(tuple(map(int, line.split('|'))))
    else:
        updates.append(list(map(int, line.split(','))))


# Parts 1 & 2

from functools import cmp_to_key

correctly_ordered_updates = list()

def compare_update_numbers(number1, number2):
    if (number1, number2) in ordering_rules:
        return -1
    elif (number2, number1) in ordering_rules:
        return 1
    else:
        return 0

correctly_ordered_updates = list() # Part 1
incorrectly_ordered_updates_sorted = list() # Part 2

for update in updates:
    sorted_update = sorted(update, key=cmp_to_key(compare_update_numbers))
    if update == sorted_update: 
        correctly_ordered_updates.append(sorted_update)
    else:
        incorrectly_ordered_updates_sorted.append(sorted_update)

def get_middle_number_sum(updates):
    return sum(update[len(update) // 2] for update in updates)

# Part 1

print(f'If we add up the middle page number of the correctly-ordered updates we get {get_middle_number_sum(correctly_ordered_updates)}.')


# Part 2

print(f'If we add up the middle page number of the incorrectly-ordered updates after sorting them we get {get_middle_number_sum(incorrectly_ordered_updates_sorted)}.')
