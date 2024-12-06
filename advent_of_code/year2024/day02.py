# Day 2

# Input

from util.get_input import get_input

def get_reports():
    return list(list(map(int, line.split(' '))) for line in get_input(2024, 2).splitlines())


# Part 1

def is_report_safe(report, decreasing = None):
    current_level = report[0]
    for level in report[1:]:
        if decreasing is None:
            decreasing = level < current_level
        else:
            if (decreasing and level > current_level) or (not decreasing and level < current_level):
                return False
        difference = abs(level - current_level)
        if difference <= 0 or difference >= 4:
            return False
        current_level = level
    return True

print(f'The number of safe reports is {sum(is_report_safe(report) for report in get_reports())}')


# Part 2

def is_report_safe_with_dampening(report):
    if not is_report_safe(report):
        for i in range(len(report)):
            if is_report_safe(report[:i] + report[i+1:]):
                return True
        return False
    return True

print(f'The number of safe reports is {sum(is_report_safe_with_dampening(report) for report in get_reports())}')
