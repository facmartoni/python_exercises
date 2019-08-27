import random

# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

# Extras:

# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.


def run():
    valid_numbers = [str(num) for num in range(1, 10)]
    print('Welcome to the Guessing Game!! If you want to quit, type exit :)')

    while True:
        random_number = random.randint(1, 9)
        count = 0

        while True:
            num_chosen = input('\nType a number between 1 and 9: ').lower()
            if num_chosen == str(random_number) and num_chosen in valid_numbers:
                print(f'\nYou win! The random number is {random_number}')
                count += 1
                break
            elif num_chosen < str(random_number) and num_chosen in valid_numbers:
                print('\nThe random number is higher')
                count += 1
            elif num_chosen > str(random_number) and num_chosen in valid_numbers:
                print('\nThe random number is lower')
                count += 1
            elif num_chosen == 'exit':
                exit()
            else:
                print('\nEnter a valid input!')

        print(f'\nYou tried {count} times, let\'s play again :D')


if __name__ == '__main__':
    run()
