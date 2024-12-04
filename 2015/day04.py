# Day 4

# Input

key = ""


# Part 1

import hashlib

def mine_advent_coins(secret_key, num_zeroes):
    i = 0
    while not verify_hash(hashlib.md5((secret_key + str(i)).encode()).hexdigest(), num_zeroes):
        i += 1
    return i
    
def verify_hash(hash, num_zeroes):
    return str(hash)[:num_zeroes] == '0' * num_zeroes

print(f"Number: {mine_advent_coins(key, 5)}")


# Part 2

print(f"Number: {mine_advent_coins(key, 6)}")
