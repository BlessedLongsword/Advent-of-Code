# Day 07

# Input

from util.get_input import get_input

def get_diagram():
    return get_input(2025, 7).splitlines()


# Part 1

def trace_beam(pos, splits, diagram, splitter):
    i, j = pos
    while diagram[i][j] != splitter:
        i += 1
        if i >= len(diagram) - 1:
            return 0
    if (i, j) in splits:
        return 0
    splits.add((i, j))
    trace_beam((i, j - 1), splits, diagram, splitter)
    trace_beam((i, j + 1), splits, diagram, splitter)
    return len(splits)

print(f"The beam is split {trace_beam((1, get_diagram()[0].index('S')), set(), get_diagram(), '^')} times.")

# Part 2

timeline_memo = dict()

def explore_timelines(pos, diagram, splitter):
    i, j = pos
    while diagram[i][j] != splitter:
        i += 1
        if i >= len(diagram) - 1:
            return 1
    if (i, j) in timeline_memo:
        return timeline_memo[(i, j)]
    explored_timelines = explore_timelines((i, j - 1), diagram, splitter) + explore_timelines((i, j + 1), diagram, splitter)
    timeline_memo[(i, j)] = explored_timelines
    return explored_timelines

print(f"The tachyon particle would end up in {explore_timelines((1, get_diagram()[0].index('S')), get_diagram(), '^')} timelines.")
