
def max_of_three(a, b, c):
    if a >= b:
        if a >= c:
            return a

    if b >= a:
        if b >= c:
            return b

    if c >= a:
        if c >= b:
            return c


def run():
    numbers = input(
        '\nGive me three numbres separated by comma, e.g "1,2,3": ')
    numbers = numbers.split(',')

    while True:
        if len(numbers) == 3:
            break
        print('\nInvalid input!')
        numbers = input(
            '\nGive me three numbres separated by comma, e.g "1,2,3": ')
        numbers = numbers.split(',')

    max_number = max_of_three(
        int(numbers[0]), int(numbers[1]), int(numbers[2]))
    print(f'\nThe max number is {max_number}')


if __name__ == '__main__':
    run()
