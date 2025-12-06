# Day 05

# Input

from math import prod
from util.get_input import get_input

OPERATIONS = {'+': lambda x: sum(x), '*': lambda x: prod(x)}

def get_column(matrix, i):
    return [matrix[j][i] for j in range(len(matrix))]

def merge_columns(c1, c2):
    return [''.join((e1, e2)) for e1, e2 in zip(c1, c2)]

def get_problems():
    horizontal_list = get_input(2025, 6).splitlines()
    raw_operands_list = horizontal_list[:-1]
    operations = [operation for operation in horizontal_list[-1].split(' ') if operation != '']
    problems = []
    counter = 0
    for i in range(len(operations)):
        current_column = get_column(raw_operands_list, counter)
        accumulated_column = ['' for _ in range(len(current_column))]
        while ''.join(current_column).strip() != '' and counter < len(raw_operands_list[0]):
            accumulated_column = merge_columns(accumulated_column, current_column)
            counter += 1
            if counter < len(raw_operands_list[0]):
                current_column = get_column(raw_operands_list, counter)
        counter += 1
        problems.append({'operation': OPERATIONS[operations[i]], 'operands': accumulated_column})
    return problems


# Part 1


def translate_problem_to_human(problem):
    operands = problem['operands']
    translated_operands = list(map(lambda x: int(x.strip()), operands))
    return {'operation': problem['operation'], 'operands': translated_operands}

def translate_problems(problems, translator):
    return [translator(problem) for problem in problems]

print(f"The grand total is {sum(problem['operation'](problem['operands']) for problem in translate_problems(get_problems(), translate_problem_to_human))}")


# Part 2

def translate_problem_to_cephalopod(problem):
    operands = problem['operands']
    max_operand_length = max(len(operand.strip()) for operand in operands)
    translated_operands = [int(''.join(operands[j][i] for j in range(len(operands)) if operands[j][i] != ' ')) for i in range(max_operand_length)]
    return {'operation': problem['operation'], 'operands': translated_operands}

print(f"The translated grand total is {sum(problem['operation'](problem['operands']) for problem in translate_problems(get_problems(), translate_problem_to_cephalopod))}")
