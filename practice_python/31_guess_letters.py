import os

# This exercise is Part 2 of 3 of the Hangman exercise series.

# Let’s continue building Hangman.
# In the game of Hangman, a clue word is given by the program that the player has to guess, letter by letter.
# The player guesses one letter at a time until the entire word has been guessed.
# (In the actual game, the player can only guess 6 letters incorrectly before losing).

# Let’s say the word the player has to guess is “EVAPORATE”.
# For this exercise, write the logic that asks a player to guess a letter and displays letters in the clue word that were guessed correctly.
# For now, let the player guess an infinite number of times until they get the entire word.
# As a bonus, keep track of the letters the player guessed and display a different message if the player tries to guess that letter again.
# Remember to stop the game when all the letters have been guessed correctly!
# Don’t worry about choosing a word randomly or keeping track of the number of guesses the player has remaining - we will deal with those in a future exercise.


def run():
    os.system('cls')
    random_word = 'programacion'.upper()
    clue_word = ['_'] * len(random_word)
    letters_guessed = set()
    print('\nWelcome to Hangman! 🪓')

    while True:
        print('\n')
        print(clue_word)

        if '_' not in clue_word:
            print(f'\nCongrats! The word was {random_word}')
            break

        letter = input('\n>>> Guess your letter: ').upper()

        if letter in letters_guessed:
            print('\nLetter already guessed!')
            continue

        letters_guessed.add(letter)

        for idx in range(len(random_word)):
            if letter == random_word[idx]:
                clue_word[idx] = letter


if __name__ == '__main__':
    run()
