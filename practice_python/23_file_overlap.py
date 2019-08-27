# Given two .txt files that have lists of numbers in them, find the numbers that are overlapping.
# One .txt file has a list of all prime numbers under 1000, and the other .txt file has a list of happy numbers up to 1000.

# (If you forgot, prime numbers are numbers that can’t be divided by any other number.
# And yes, happy numbers are a real thing in mathematics - you can look it up on Wikipedia.


def run():

    # Reading and saving prime numbers
    with open('primes.txt', 'r') as f:
        prime_numbers = f.read().split('\n')

    # Reading and saving happy numbers
    with open('happy_numbers.txt', 'r') as f:
        happy_numbers = f.read().split('\n')

    overlapping_numbers = []

    # Searching the numbers that are overlapping
    for num in happy_numbers:
        if num in prime_numbers:
            overlapping_numbers.append(num)

    # print(len(prime_numbers))
    # print(len(happy_numbers))

    print(f'Overlapping numbers: {overlapping_numbers}')


if __name__ == '__main__':
    run()
