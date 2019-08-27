dollarValue = 45.51


def dollarToArgentinePesos(ammount):
    return ammount * dollarValue


def run():
    print('C O N V E R S O R  D E  D I V I S A S')
    print('Convierte dólares a pesos argentinos')
    print('')

    ammount = float(input('Ingresa la cantidad de dólares: '))
    converted = dollarToArgentinePesos(ammount)
    print('')
    print('Son ${} pesos argentinos'.format(converted))


if __name__ == '__main__':
    run()
