# Day 5

# Input

def get_strings(file):
    return open(file).read().splitlines()


# Part 1

import re

part1_rules = r".*(?=.*(.)\1{1,}.*)(?=.*[aeiou].*[aeiou].*[aeiou].*)(?=^(?:(?!(ab)|(cd)|(pq)|(xy)).)*$).*"

def count_nice_strings(strings, rules):
    return sum([re.match(rules, string) != None for string in strings])

print("There are", count_nice_strings(get_strings("input.txt"), part1_rules), "nice strings.")


# Part 2

part2_rules = r".*(?=.*(..).*\1.*)(?=.*(.).\2).*"

print("There are", count_nice_strings(get_strings("input.txt"), part2_rules), "nice strings under the new rules.")


# I went for regular expressions with this one as I believe it was a nice opportunity to learn more about them. 
