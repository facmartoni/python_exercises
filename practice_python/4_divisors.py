# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)


def run():
    number = int(input('Type a number: '))
    divisors = [divisor for divisor in range(
        1, number + 1) if number % divisor == 0]
    print(f'The divisors of {number} are {divisors}')


if __name__ == '__main__':
    run()
