# Day 7

# Input + Parts 1 & 2

from util.get_input import get_input

class Equation:
    def __init__(self, result, operands, valid_operators):
        self.result = result
        self.operands = operands
        self.operators = valid_operators

    def is_solvable(self):
        def operate_and_explore(acc, operand_index, operator):
            acc = operator(acc, self.operands[operand_index])
            if operand_index == len(self.operands) - 1:
                return acc == self.result
            if acc > self.result:
                return False
            return any(operate_and_explore(acc, operand_index + 1, op) for op in self.operators)
        return any(operate_and_explore(self.operands[0], 1, op) for op in self.operators)
    
    def __str__(self):
        return f'{self.result}: {self.operands}'


def get_calibration_equations(valid_operators):
    equations = list()
    for line in get_input(2024, 7).splitlines():
        result, operands = line.split(': ')
        result = int(result)
        operands = list(map(int, operands.split(' ')))
        equations.append(Equation(result, operands, valid_operators))
    return equations


# Part 1

def add(a, b):
    return a + b

def mul(a, b):
    return a * b

operators_part1 = [add, mul]

print(f'The total calibration result of the true equations is {sum(equation.result for equation in get_calibration_equations(operators_part1) if equation.is_solvable())}.')


# Part 2

def con(a, b):
    return int(str(a) + str(b))

operators_part2 = [add, mul, con]

print(f'The total calibration result of the true equations after adding concatenation is {sum(equation.result for equation in get_calibration_equations(operators_part2) if equation.is_solvable())}.')
