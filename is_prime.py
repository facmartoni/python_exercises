
def isPrime(number):
    if(number < 2):
        return False
    if(number == 2):
        return True
    if(number > 2 and number % 2 == 0):
        return False

    for i in range(3, number):
        if(number % i == 0):
            return False

    return True


def run():
    number = int(input('Escribe un número: '))
    if(isPrime(number)):
        print('\n Es primo')
    else:
        print('\n No es primo')


if __name__ == '__main__':
    run()
