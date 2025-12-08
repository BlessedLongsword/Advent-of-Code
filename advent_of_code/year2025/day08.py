# Day 8

"""
TODO: This works but is basically brute force and I do not like it :/
"""

# Input

from math import prod, sqrt
from util.get_input import get_input

def get_boxes_positions():
    return list(map(lambda x: tuple(map(int, x.split(','))), get_input(2025, 8).splitlines()))

# Part 1

def get_distance(pos1, pos2):
    x1, y1, z1 = pos1
    x2, y2, z2 = pos2
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)

def get_distances(positions):
    distances = dict()
    for i in range(0, len(positions)):
        for j in range(i + 1, len(positions)):
            p1, p2 = positions[i], positions[j]
            distances[(p1, p2)] = get_distance(p1, p2)
    return distances

def get_connections(sorted_pairs, n):
    connections = dict()
    used_strings = 0
    idx = 0
    while used_strings < n:
        box1, box2 = sorted_pairs[idx]
        used_strings += 1
        if box1 in connections:
            connections[box1].add(box2)
        else:
            connections[box1] = {box2}
        if box2 in connections:
            connections[box2].add(box1)
        else:
            connections[box2] = {box1}
        idx += 1
    return connections

def explore_circuit(circuit, box, connections):
    circuit.add(box)
    for connection in connections[box]:
        if connection not in circuit:
            explore_circuit(circuit, connection, connections)
    return circuit

def connect_closest_boxes(positions, n):
    sorted_pairs = list(dict(sorted(get_distances(positions).items(), key=lambda item: item[1])).keys())
    connections = get_connections(sorted_pairs, n)
    circuits = []
    while connections:
        circuit = explore_circuit(set(), next(iter(connections.keys())), connections)
        circuits.append(circuit)
        for box in circuit:
            connections.pop(box, None)
    return circuits

print(f'If we multiply the sizes of the three largest circuits we get {prod(list(sorted(map(len, connect_closest_boxes(get_boxes_positions(), 10)), key=lambda x: -x))[:3])}')

# Part 2

def print_connections(connections):
    for connection in connections:
        print(f'{connection}: {connections}')

def get_last_connection(positions):
    sorted_pairs = list(dict(sorted(get_distances(positions).items(), key=lambda item: item[1])).keys())
    box1, box2 = sorted_pairs[0]
    connections = {box1: {box2}, box2: {box1}}
    idx = 1
    while len(explore_circuit(set(), next(iter(connections.keys())), connections)) < len(positions):
        box1, box2 = sorted_pairs[idx]
        if box1 in connections:
            connections[box1].add(box2)
        else:
            connections[box1] = {box2}
        if box2 in connections:
            connections[box2].add(box1)
        else:
            connections[box2] = {box1}
        idx += 1
    return (box1, box2) 

print(f'If we multiply the X coordinates of the last two junction boxes to connect we get {prod(map(lambda e: e[0], get_last_connection(get_boxes_positions())))}')
