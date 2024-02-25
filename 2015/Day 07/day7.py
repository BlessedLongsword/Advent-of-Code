"""
--- Day 7: Some Assembly Required ---

This year, Santa brought little Bobby Tables a set of wires and bitwise logic gates! Unfortunately, little Bobby is a 
little under the recommended age range, and he needs help assembling the circuit.

Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal (a number from 0 to 65535). 
A signal is provided to each wire by a gate, another wire, or some specific value. Each wire can only get a signal 
from one source, but can provide its signal to multiple destinations. A gate provides no signal until all of its inputs have a signal.

The included instructions booklet describes how to connect the parts together: x AND y -> z means to 
connect wires x and y to an AND gate, and then connect its output to wire z.

For example:

    123 -> x means that the signal 123 is provided to wire x.
    x AND y -> z means that the bitwise AND of wire x and wire y is provided to wire z.
    p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2 and then provided to wire q.
    NOT e -> f means that the bitwise complement of the value from wire e is provided to wire f.

Other possible gates include OR (bitwise OR) and RSHIFT (right-shift). If, for some reason, you'd like to emulate 
the circuit instead, almost all programming languages (for example, C, JavaScript, or Python) provide operators for these gates.

For example, here is a simple circuit:

123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i

After it is run, these are the signals on the wires:

d: 72
e: 507
f: 492
g: 114
h: 65412
i: 65079
x: 123
y: 456

In little Bobby's kit's instructions booklet (provided as your puzzle input), what signal is ultimately provided to wire a?

"""

def get_circuit(file):
    return open(file).read().splitlines()

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
#Your puzzle answer was 46065

"""
--- Part Two ---
Now, take the signal you got on wire a, override wire b to that signal, and reset 
the other wires (including wire a). What new signal is ultimately provided to wire a?
"""

#We just change the input

print(run_circuit(get_circuit("input_pt2.txt")), "is the new signal provided to wire a.")