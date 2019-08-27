import random

# This exercise is Part 1 of 3 of the Hangman exercise series.

# In this exercise, the task is to write a function that picks a random word from a list of words from the SOWPODS dictionary.
# Download this file and save it in the same directory as your Python code.
# This file is Peter Norvig’s compilation of the dictionary of words used in professional Scrabble tournaments.
# Each line in the file contains a single word.

# Hint: use the Python random library for picking a random word.


def put_lines_in_a_list(filename):
    with open(filename, 'r') as f:
        lines_list = f.read().split('\n')
    return lines_list


def run():
    words_list = put_lines_in_a_list('sowpods.txt')
    random_word = random.choice(words_list)
    print('\n' + random_word)
    print(f'\nThere are {len(words_list)} words in the SOWPODS dictionary')


if __name__ == '__main__':
    run()
