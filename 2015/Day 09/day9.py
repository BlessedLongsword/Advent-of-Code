"""
--- Day 9: All in a Single Night ---

Every year, Santa manages to deliver all of his presents in a single night.

This year, however, he has some new locations to visit; his elves have provided him the distances between every 
pair of locations. He can start and end at any two (different) locations he wants, but he must visit each location 
exactly once. What is the shortest distance he can travel to achieve this?

For example, given the following distances:

London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141

The possible routes are therefore:

Dublin -> London -> Belfast = 982
London -> Dublin -> Belfast = 605
London -> Belfast -> Dublin = 659
Dublin -> Belfast -> London = 659
Belfast -> Dublin -> London = 605
Belfast -> London -> Dublin = 982

The shortest of these is London -> Dublin -> Belfast = 605, and so the answer is 605 in this example.

What is the distance of the shortest route?
"""

from itertools import permutations    
        
def get_cities(file):
    cities = {}
    for trip in open(file).read().splitlines():
        pair, distance = trip.split(' = ')
        origin, dest = pair.split(' to ')
        if origin in cities:
            cities[origin][dest] = int(distance)
        else:
            cities[origin] = {dest: int(distance)}
        if dest in cities:
            cities[dest][origin] =  int(distance)
        else:
            cities[dest] = {origin: int(distance)} 
    return cities


def shortest_route(cities):
    min_dist = float('inf')
    for route in permutations(cities):
        traveled_dist = 0
        for i in range(len(route) - 1):
            traveled_dist += cities[route[i]][route[i + 1]]
        min_dist = min(min_dist, traveled_dist)
    return min_dist
            
                
print("The distance of the shortest route is", shortest_route(get_cities("input.txt")))

"""
--- Part Two ---
The next year, just to show off, Santa decides to take the route with the longest distance instead.

He can still start and end at any two (different) locations he wants, and he still must visit each location exactly once.

For example, given the distances above, the longest route would be 982 via (for example) Dublin -> London -> Belfast.

What is the distance of the longest route?
"""

def longest_route(cities):
    max_dist = 0
    for route in permutations(cities):
        traveled_dist = 0
        for i in range(len(route) - 1):
            traveled_dist += cities[route[i]][route[i + 1]]
        max_dist = max(max_dist, traveled_dist)
    return max_dist

print("The distance of the longest route is", longest_route(get_cities("input.txt")))