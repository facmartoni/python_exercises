import json
import time
import os

# This exercise is Part 2 of 4 of the birthday data exercise series.
# In the previous exercise we created a dictionary of famous scientists’ birthdays.
# In this exercise, modify your program from Part 1 to load the birthday dictionary from a JSON file on disk, rather than having the dictionary defined in the program.
# Bonus: Ask the user for another scientist’s name and birthday to add to the dictionary, and update the JSON file you have on disk with the scientist’s name.
# If you run the program multiple times and keep adding new names, your JSON file should keep getting bigger and bigger.


def display_menu():
    os.system('cls')
    choice = input('''
    Welcome to the birthday dictionary!! 🎈🎈🎈

    [b]irthdays
    [a]dd birthday
    [s]earch birthday
    [q]uit

    Enter an option: ''')
    return choice


def see_birthdays():
    os.system('cls')
    try:
        with open('birthdays.json', 'r') as f:
            birthdays = json.load(f)
        print('We know the birthdays of:\n')
        for key, value in birthdays.items():
            print(f'{key}: {value}')
    except:
        print("We don't have birthdays yet 🙁")
    input('\nPress enter to return to the menu...')


def add_birthday():
    os.system('cls')
    name = input('Enter the name of the person: ').title()
    birthday = input(f'Enter the birthday of {name}: ')

    try:
        with open('birthdays.json', 'r') as f:
            birthdays = json.load(f)
    except:
        birthdays = {}
    birthdays[name] = birthday
    with open('birthdays.json', 'w') as f:
        json.dump(birthdays, f)

    print(f'\n{name} succesfully added!')
    input('\nPress enter to return to the menu...')


def search_birthday():
    os.system('cls')
    try:
        with open('birthdays.json', 'r') as f:
            birthdays = json.load(f)
        name = input("Whose birthday do you want to know?: ").title()
        if name in birthdays:
            print('\n' + birthdays[name])
        else:
            print("\nWe don't know that person 🙁")
    except:
        print("We don't have birthdays yet 🙁")
    input('\nPress enter to return to the menu...')


def run():
    choice = display_menu()
    while choice != 'q':
        if choice == 'b':
            see_birthdays()
        elif choice == 'a':
            add_birthday()
        elif choice == 's':
            search_birthday()
        else:
            print('\nInvalid option!')
            time.sleep(1)
        choice = display_menu()


if __name__ == '__main__':
    run()
