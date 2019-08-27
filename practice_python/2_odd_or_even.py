# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

# Extras:

# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.


def run():
    number = int(input('Choose a random number: '))

    if number % 4 == 0:
        print('Your number is a multiple of 4')
    elif number % 2 == 0:
        print('Your number is even')
    else:
        print('Your number is odd')

    while True:
        num = int(input('Now, give me a number to check, except 0: '))
        if(num == 0):
            print('Other than 0, please!')
            continue
        break
    check = int(input('And a number to divide by: '))

    if(check % num == 0):
        print(f'{check} divides evenly into {num}')
    else:
        print(f"{check} doesn't divides evenly into {num}")


if __name__ == '__main__':
    run()
