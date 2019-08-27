import os

# This exercise is Part 1 of 4 of the birthday data exercise series.

# For this exercise, we will keep track of when our friend’s birthdays are, and be able to find that information based on their name.
# Create a dictionary (in your file) of names and birthdays.
# When you run your program it should ask the user to enter a name, and return the birthday of that person back to them.
# The interaction should look something like this:

# >>> Welcome to the birthday dictionary. We know the birthdays of:
# Albert Einstein
# Benjamin Franklin
# Ada Lovelace
# >>> Who's birthday do you want to look up?
# Benjamin Franklin
# >>> Benjamin Franklin's birthday is 01/17/1706.

BIRTHDAYS = {
    'Gaston Costas': '01/01/0000',
    'Gaston Gonzalez': '02/01/0000',
    'Jose Diaz': '03/01/0000',
    'Marcio Riviere': '04/01/0000',
    'Ignacio Gonzalez Ley': '05/01/0000'
}


def run():
    os.system('cls')
    print('Welcome to the birthday dictionary!! 🎈🎈🎈')
    print(f'\nWe know the birthdays of:\n')
    for key in BIRTHDAYS.keys():
        print(key)
    name = input("\nWho's birthday do you want to look up?: ").title()

    try:
        print(f"\n{name}'s birthday is {BIRTHDAYS[name]} 🎉")
    except KeyError:
        print("\nWe don't know that person 🙁")


if __name__ == '__main__':
    run()
