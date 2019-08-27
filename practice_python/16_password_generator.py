import os
import random

# Write a password generator in Python.
# Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
# The passwords should be random, generating a new password every time the user asks for a new password.
# Include your run-time code in a main method.

# Extra:

# Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.

words = ['hola', 'cafe', 'hospital', 'python', 'casa',
         'tutu', 'camion', 'camioneta', 'celular', 'computadora']
lowercase_letters = list('qwertyuiopasdfghjklñzxcvbnm')
uppercase_letters = list('QWERTYUIOPASDFGHJKLÑZXCVBNM')
numbers = list('0123456789')
symbols = list('!"#$%&/()=?¡')
letters = [lowercase_letters, uppercase_letters]
characters = [lowercase_letters, uppercase_letters, numbers, symbols]


def strong_password():
    strong_password = []
    for number in range(random.randint(8, 65)):
        strong_password.append(
            random.choice(random.choice(characters))
        )
    return ''.join(strong_password)


def normal_password():
    normal_password = []
    for number in range(random.randint(8, 33)):
        normal_password.append(
            random.choice(random.choice(letters))
        )
    return ''.join(normal_password)


def weak_password():
    number_of_words = random.randint(1, 2)
    if number_of_words == 1:
        return random.choice(words)
    else:
        return random.choice(words) + random.choice(words)


def display_menu():
    os.system('cls')
    choice = input('''
            Password Generator

            [s]trong password
            [n]ormal password
            [w]eak password
            [q]uit
        
        ''')
    return choice


def run():
    choice = display_menu()
    while (choice != 'q'):
        os.system('cls')
        if(choice == 's'):
            print(strong_password())
        elif(choice == 'n'):
            print(normal_password())
        elif(choice == 'w'):
            print(weak_password())
        else:
            print('\n Invalid input!')
        input('\nPress enter to return to the menu...')
        choice = display_menu()


if __name__ == '__main__':
    run()
