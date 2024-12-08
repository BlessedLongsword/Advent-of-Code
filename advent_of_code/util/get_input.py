import os, requests
from datetime import datetime


def build_input_filename(year, day, example = False):
    prefix = '0' if day < 10 else ''
    suffix = '_example' if example else ''
    return f'./year{year}/inputs/day{prefix}{day}{suffix}.txt'

def get_input(year, day, example = False):
    if year < 2015:
        raise ValueError('AOC Started on 2015 man, invalid year')
    if year > datetime.now().year:
        raise ValueError('Bro lives in the future, invalid year')
    if not 0 < day < 26:
        raise ValueError('AOC is an ADVENT CALENDAR, invalid day')
    filename = build_input_filename(year, day, example)
    if not os.path.isfile(filename) and not example:
        url = f'https://adventofcode.com/{year}/day/{day}/input'
        cookies = {'session': os.getenv('AOC_SESSION')}
        r = requests.get(url, cookies=cookies)
        r.raise_for_status()
        f = open(filename, 'w')
        f.write(r.text)
        f.close()
    with open(filename) as file:
        return file.read()
