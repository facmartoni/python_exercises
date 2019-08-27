
def factorial(number):
    if(number == 0):
        return 1
    return number * factorial(number - 1)


def run():
    number = int(input('\nIngresa un número para saber su factorial: '))
    result = factorial(number)
    print('\nEl factorial de {} es: {} \n'.format(number, result))


if __name__ == '__main__':
    run()
