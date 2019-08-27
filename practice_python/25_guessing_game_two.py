import random
import os
import time

# In a previous exercise, we’ve written a program that “knows” a number and asks a user to guess it.

# This time, we’re going to do exactly the opposite.
# You, the user, will have in your head a number between 0 and 100.
# The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.

# At the end of this exchange, your program should print out how many guesses it took to get your number.

# As the writer of this program, you will have to choose how your program will strategically guess.
# A naive strategy can be to simply start the guessing at 1, and keep going (2, 3, 4, etc.) until you hit the number.
# But that’s not an optimal guessing strategy.
# An alternate strategy might be to guess 50 (right in the middle of the range), and then increase / decrease by 1 as needed.
# After you’ve written the program, try to find the optimal strategy!
# (We’ll talk about what is the optimal one next week with the solution.)


def display_menu():
    os.system('cls')
    choice = input('''
    Guessing Game Two

    [p]lay
    [i]nstructions
    [q]uit

    Enter an option: ''')
    return choice


def display_instructions():
    os.system('cls')
    print('''
    Hello user! I am the machine :)

    This time, you will think in a number between 0 and 100
    I will try to guess it, and you have to say me these things:

    - The number I thought is too [l]ow
    - The number I thought is too [h]igh
    - The number I thought is your [n]umber!

    Don´t make me suffer, please D: 
    ''')
    input('\nPress enter to return to the menu...')


def search_number(min_number, max_number):
    return (min_number + max_number) // 2


def play():
    os.system('cls')
    input("Do you have your number in mind? Press enter to begin!")
    os.system('cls')

    tries = 1
    min_number = 0
    max_number = 100
    number = random.randint(0, 100)
    while True:
        print(f'\n I guess... {number} 🤔')

        decision = input('\n[h]igh, [l]ow or exactly [n]umber: ')
        while decision != 'h' and decision != 'l' and decision != 'n':
            print('\nEnter a valid option :(')
            decision = input('\n[h]igh, [l]ow or exactly [n]umber: ')

        if decision == 'n':

            if tries == 1:
                plural_or_singular = ''
            else:
                plural_or_singular = 's'

            print(
                f'\nYeah! I win! :D I tried {tries} time{plural_or_singular} for searching {number}')

            input('\nPress enter to return to the menu...')

            break

        if decision == 'l':
            min_number = number + 1

        if decision == 'h':
            max_number = number - 1

        number = search_number(min_number, max_number)
        tries += 1


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
