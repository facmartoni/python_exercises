import math

# Ask the user for a number and determine whether the number is prime or not.
# (For those who have forgotten, a prime number is a number that has no divisors.).
# You can (and should!) use your answer to Exercise 4 to help you.
# Take this opportunity to practice using functions, described below.


def is_prime(number):
    if number <= 1:
        return False
    elif number == 2 or number == 3:
        return True
    elif number % 2 == 0:
        return False
    else:
        for num in range(3, int(math.sqrt(number)) + 1, 2):
            if number % num == 0:
                return False
        return True


def run():
    number = int(input('Give me a number: '))
    if(is_prime(number)):
        print('Is prime')
    else:
        print('Is not prime')
    # primes = {num: is_prime(num) for num in range(number + 1)}
    # print(primes)


if __name__ == '__main__':
    run()
