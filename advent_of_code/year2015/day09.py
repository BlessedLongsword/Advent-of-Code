# Day 9

# Input
        
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


# Part 1

from itertools import permutations    

def shortest_route(cities):
    min_dist = float('inf')
    for route in permutations(cities):
        traveled_dist = 0
        for i in range(len(route) - 1):
            traveled_dist += cities[route[i]][route[i + 1]]
        min_dist = min(min_dist, traveled_dist)
    return min_dist
            
                
print("The distance of the shortest route is", shortest_route(get_cities("input.txt")))


# Part 2

def longest_route(cities):
    max_dist = 0
    for route in permutations(cities):
        traveled_dist = 0
        for i in range(len(route) - 1):
            traveled_dist += cities[route[i]][route[i + 1]]
        max_dist = max(max_dist, traveled_dist)
    return max_dist

print("The distance of the longest route is", longest_route(get_cities("input.txt")))
