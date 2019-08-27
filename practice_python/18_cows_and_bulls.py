import random
import os
import time

# Create a program that will play the “cows and bulls” game with the user. The game works like this:

# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.

# Say the number generated by the computer is 1038. An example interaction could look like this:

#   Welcome to the Cows and Bulls Game!
#   Enter a number:
#   >>> 1234
#   2 cows, 0 bulls
#   >>> 1256
#   1 cow, 1 bull
#   ...
# Until the user guesses the number.


def display_presentation():
    os.system('cls')
    print('''
  ___________________________________
< Welcome to the Cows and Bulls game! >
  -----------------------------------
         \   ^__^ 
          \  (oo)\_______
             (__)\       )\/
                 ||----w |
                 ||     ||
    ''')
    time.sleep(3)


def display_menu():
    os.system('cls')
    choice = input('''
    --- * --- * --- * --- * --- * --- * 
    [p]lay
    [i]nstructions
    [q]uit
    --- * --- * --- * --- * --- * --- * 

    Enter an option: ''')
    return choice


def play():
    os.system('cls')

    print('Enter a number:')

    random_number = list(str(random.randint(1000, 9999)))
    # random_number = ['2', '0', '0', '1'] # Debug line

    tries = 1
    number = list(input('\n>>> '))
    while(number != random_number):
        if len(number) == 4:
            # CURIOSO error; las listas se pueden duplicar unicamente así, sino ambas variables representan al mismo objeto en memoria.
            temp_random_number = random_number[:]
            temp_number = number[:]
            cows = 0
            bulls = 0

            # Searching for cows
            for idx, i in enumerate(temp_number):
                if i in temp_random_number and temp_random_number[idx] == i:
                    cows += 1
                    temp_random_number[idx] = '*'
                    temp_number[idx] = '*'

            # Searching for bulls
            for idx, i in enumerate(temp_number):
                if i != '*' and i in temp_random_number:
                    bulls += 1
                    position_of_i = temp_random_number.index(i)
                    temp_random_number[position_of_i] = '*'
                    temp_number[idx] = '*'

            print(f'\n{cows} cows, {bulls} bulls')
            tries += 1
        else:
            print('\nEnter a valid number!')
        number = list(input('\n>>> '))

    random_number = ''.join(random_number)
    print(f'\nCongratulations! You win! You tried {tries} times :)')
    print(f'\nThe number was {random_number}')
    input('\nPress enter to return to the menu...')


def display_instructions():
    os.system('cls')
    print('''
    How to play?

    The machine generates a random 4-digit number. 
    Your task is guess that number.
    When you guess correctly a digit and its position, you get a cow.
    When you guess correctly a digit but not its position, you get a bull.
    So, when you get four cows, you win :)

    Let's have fun!
    ''')
    input('\nPress enter to return to the menu...')


def run():
    display_presentation()
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
