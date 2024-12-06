# Day 4

# Input

from util.get_input import get_input

def get_word_search():
    return get_input(2024, 4).splitlines()


# Part 1

def is_word_in_direction(word_search, word, position, direction):
    height = len(word_search)
    width = len(word_search[0])
    i, j = position
    if not (0 <= i < height and 0 <= j < width):
        return False
    di, dj = direction
    if not (-1 <= di <= 1 and -1 <= dj <= 1):
        return False
    ti, tj = i + di * (len(word) - 1), j + dj * (len(word) - 1)
    if not (0 <= ti < height and 0 <= tj < width):
        return False
    for k in range(len(word)):
        if not word[k] == word_search[i + di * k][j + dj * k]:
            return False
    return True

def count_words_in_word_search(word_search, word):
    acc = 0
    for i in range(len(word_search)):
        for j in range(len(word_search[0])):
            if word_search[i][j] == word[0]:
                for direction in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                    acc += int(is_word_in_direction(word_search, word, (i, j), direction))
    return acc

print(f'XMAS appears {count_words_in_word_search(get_word_search(), 'XMAS')} times')


# Part 2

def count_crosses_in_word_search(word_search, word):
    if len(word) % 2 == 0:
        return 'Can\'t be a cross XD'
    acc = 0
    for i in range(len(word_search)):
        for j in range(len(word_search[0])):
            if word_search[i][j] == word[len(word) // 2]:
                acc += int((is_word_in_direction(word_search, word, (i - 1, j - 1), (1, 1)) or \
                        is_word_in_direction(word_search, word, (i + 1, j + 1), (-1, -1))) and \
                        (is_word_in_direction(word_search, word, (i + 1, j - 1), (-1, 1)) or \
                        is_word_in_direction(word_search, word, (i - 1, j + 1), (1, -1))))
    return acc

print(f'X-MAS appears {count_crosses_in_word_search(get_word_search(), 'MAS')} times')
