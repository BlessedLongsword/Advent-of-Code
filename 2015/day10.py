# Day 10

# Input

key = ""


# Part 1

def look_and_say(sequence, rounds):
    
    while rounds > 0:
        
        rounds -= 1
        
        new_sequence = ""
        prev = None
        equal_count = 0
        for digit in sequence:
            if prev and digit != prev:
                new_sequence += str(equal_count) + prev
                equal_count = 0
            equal_count += 1
            prev = digit
            
        sequence = new_sequence + str(equal_count) + prev
    
    return len(sequence)

print(look_and_say(key, 40))


# Part 2

print(look_and_say(key, 50))
