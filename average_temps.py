def average(list):
    acum = 0
    for element in list:
        acum += element

    result = acum / len(list)
    return round(result, 2)


def run():
    temps = [21, 24, 24, 22, 20, 23, 24]
    print(f'El promedio de temperaturas es {average(temps)}')


if __name__ == '__main__':
    run()
