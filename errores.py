

def run():

    countries = {
        'mexico': 122,
        'colombia': 49,
        'argentina': 43,
        'chile': 18,
        'peru': 31
    }

    while True:
        try:
            country = input(
                '¿De que país quieres saber la población?: ').lower()
            print(
                f'La población de {country} es {countries[country]} millones\n')
        except KeyError:
            print('No tenemos ese país en la base de datos :(\n')


if __name__ == '__main__':
    run()
