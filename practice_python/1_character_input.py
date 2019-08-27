from datetime import date

# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

# Extras:

# Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
# Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)


def run():
    name = input('Your name: ')
    age = int(input('Your age: '))
    copies_of_message = int(input('Quantity of messages you want: '))
    actual_year = date.today().year
    year_in_100_years_old = actual_year + 100 - age

    for i in range(0, copies_of_message):
        print(f"{name}, in {year_in_100_years_old} you'll have 100 years old :/")


if __name__ == '__main__':
    run()
