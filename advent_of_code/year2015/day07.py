# Day 7

# Input

def get_circuit(file):
    return open(file).read().splitlines()


# Part 1

class Operation:
    def __init__(self, operand, target, second_operand=None, operator=None) -> None:
        self.operand = operand
        self.second_operand = second_operand
        self.operator = operator
        self.target = target
    
    def __str__(self):
        return f"{self.operand}, {self.second_operand}, {self.operator}, {self.target}"
    
    def operable(self, signals):
        if not self.second_operand or self.second_operand.isnumeric():
            if self.operand.isnumeric():
                return True
            return signals[self.operand] != None
        if self.operand.isnumeric():
            return signals[self.second_operand] != None
        return  signals[self.operand] != None and signals[self.second_operand] != None
    
    def operate(self, signals):
        operand_value = signals[self.operand] if not self.operand.isnumeric() else int(self.operand)
        if self.second_operand:
            second_operand_value = signals[self.second_operand] if not self.second_operand.isnumeric() else int(self.second_operand)
        if not self.operator:
            signals[self.target] = operand_value
        else:
            if self.operator == 'NOT':
                signals[self.target] = ~ operand_value
            elif self.operator == 'OR':
                signals[self.target] = operand_value | second_operand_value
            elif self.operator == 'AND':
                signals[self.target] = operand_value & second_operand_value
            elif self.operator == 'LSHIFT':
                signals[self.target] = operand_value << second_operand_value
            elif self.operator == 'RSHIFT':
                signals[self.target] = operand_value >> second_operand_value
            
def run_circuit(circuit):
    
    signals = {}
    operations = []
    
    for instruction in circuit:
        
        operation, target = instruction.split(' -> ')
        operation = operation.split(' ')
        
        if len(operation) == 1:
            operations.append(Operation(operation[0], target))
        elif len(operation) == 2:   
            operations.append(Operation(operation[1], target, operator=operation[0]))
        else:
            if operation[0].isnumeric():
                operations.append(Operation(operation[2], target, second_operand=operation[0], operator=operation[1]))
            else:   
                operations.append(Operation(operation[0], target, second_operand=operation[2], operator=operation[1]))
                
        signals[target] = None
        
    while operations:
        operation = operations.pop(0)
        if operation.operable(signals):
            operation.operate(signals)
        else:
            operations.append(operation)
            
    return signals['a']
        
print(run_circuit(get_circuit("input.txt")), "is the signal provided to wire a.")


# Part 2

print(run_circuit(get_circuit("input_pt2.txt")), "is the new signal provided to wire a.")
