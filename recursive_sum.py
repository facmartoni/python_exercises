def recursive_natural_sum(a, b):
    if b == 0:
        if a == 0:
            return 0
        return 1
    return a + recursive_natural_sum(1, b - 1)


def recursive_sum(a, b):
    # a siempre será menor que b para que la función trabaje correctamente
    if a > b:
        aux = a
        a = b
        b = aux
    if a < 0 and b < 0:
        a = abs(a)
        b = abs(b)
        return -recursive_natural_sum(a, b)
    return recursive_natural_sum(a, b)


def run():
    while True:
        a = int(input('Ingrese a: '))
        b = int(input('Ingrese b: '))
        print(recursive_sum(a, b))


if __name__ == '__main__':
    run()
