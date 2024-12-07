# Day 2

# Input

from util.get_input import get_input

def get_reports():
    return list(list(map(int, line.split(' '))) for line in get_input(2024, 2).splitlines())


# Part 1

def levels_follow_conditions(level, next_level, variation):
    difference = next_level - level
    if not 0 < abs(difference) < 4:
        return False, variation
    if variation < 0:
        return difference < 0, variation
    elif variation > 0:
        return difference > 0, variation
    else:
        return True, -1 if difference < 0 else 1
    return True, variation
        
def is_report_safe(report, variation = 0):
    for i in range(len(report) - 1):
        level, next_level = report[i], report[i + 1]
        _levels_follow_conditions, variation = levels_follow_conditions(level, next_level, variation)
        if not _levels_follow_conditions:
            return False
    return True

print(f'The number of safe reports is {sum(is_report_safe(report) for report in get_reports())}')


# Part 2

def is_report_safe_with_dampening(report, variation = 0):
    for i in range(len(report) - 1):
        level, next_level = report[i], report[i + 1]
        _levels_follow_conditions, variation = levels_follow_conditions(level, next_level, variation)
        if not _levels_follow_conditions:
            if i == len(report) - 1:
                return True
            elif i == 1:
                return is_report_safe(report[0:1] + report[2:]) or is_report_safe(report[1:])
            else:
                return is_report_safe(report[0:i] + report[i + 1:]) or is_report_safe(report[0:i + 1] + report[i + 2:])
    return True

print(f'The number of safe reports is {sum(is_report_safe_with_dampening(report) for report in get_reports())}')
