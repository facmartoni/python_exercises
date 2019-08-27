import os
import random
import time

# This exercise is Part 3 of 3 of the Hangman exercise series.

# You can start your Python journey anywhere, but to finish this exercise you will have to have finished Parts 1 and 2 or use the solutions (Part 1 and Part 2).

# In this exercise, we will finish building Hangman. In the game of Hangman, the player only has 6 incorrect guesses (head, body, 2 legs, and 2 arms) before they lose the game.

# In Part 1, we loaded a random word list and picked a word from it.
# In Part 2, we wrote the logic for guessing the letter and displaying that information to the user.
# In this exercise, we have to put it all together and add logic for handling guesses.

# Copy your code from Parts 1 and 2 into a new file as a starting point.
# Now add the following features:

# Only let the user guess 6 times, and tell the user how many guesses they have left.
# Keep track of the letters the user guessed.
# If the user guesses a letter they already guessed, don’t penalize them - let them guess again.
# Optional additions:

# When the player wins or loses, let them start a new game.
# Rather than telling the user "You have 4 incorrect guesses left", display some picture art for the Hangman.
# This is challenging - do the other parts of the exercise first!
# Your solution will be a lot cleaner if you make use of functions to help you!

IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''']


def display_menu():
    os.system('cls')
    choice = input('''
    Welcome to Hangman! 🪓

    [p]lay
    [i]nstructions
    [q]uit

    Enter an option: ''')
    return choice


def display_instructions():
    os.system('cls')
    print('''
    How to play Hangman? 🤔

    The computer will choose a secret word, and you have
    to guess it letter by letter. You have 6 opportunities
    to give a wrong letter before losing, so be careful

    Enjoy! 😎''')
    input('\nPress enter to return to the menu...')


def random_word_of_file(filename):
    with open(filename, 'r') as f:
        lines_list = f.read().split('\n')
    return random.choice(lines_list)


def play():
    os.system('cls')
    random_word = random_word_of_file('sowpods.txt')
    clue_word = ['_'] * len(random_word)
    letters_guessed = set()
    tries_left = 8

    def retry():
        retry = input('\nDo you want to keep playing? [y]es, [n]o: ')
        while retry != 'y' and retry != 'n':
            print('\nEnter a valid choice')
            retry = input('\nDo you want to keep playing? [y]es, [n]o: ')
        return retry

    while True:
        os.system('cls')
        print(IMAGES[abs(tries_left - 8)])
        print('\n')
        print(clue_word)

        if '_' not in clue_word:
            print(f'\nCongrats! The word was {random_word}')
            decision = retry()

            if decision == 'y':
                play()
                break
            elif decision == 'n':
                input('\nPress enter to return to the menu...')
                break

        letter = input(
            f'\n>>> Guess your letter: ').upper()

        if len(letter) > 1:
            print('\nEnter a valid letter!')
            time.sleep(1)
            continue

        if letter in letters_guessed:
            print('\nLetter already guessed!')
            time.sleep(1)
            continue

        letters_guessed.add(letter)

        if letter not in random_word:
            tries_left -= 1

        if tries_left == 1:
            print('\nOh.. you lose :(')
            decision = retry()

            if decision == 'y':
                play()
                break
            elif decision == 'n':
                input('\nPress enter to return to the menu...')
                break

        for idx in range(len(random_word)):
            if letter == random_word[idx]:
                clue_word[idx] = letter


def run():
    choice = display_menu()
    while choice != 'q':
        if choice == 'p':
            play()
        elif choice == 'i':
            display_instructions()
        else:
            print('\nInvalid option!')
            time.sleep(1)
        choice = display_menu()


if __name__ == '__main__':
    run()
