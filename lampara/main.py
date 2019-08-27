import time
import os
from lamp import Lamp


def run():
    lamp = Lamp(is_turned_on=True)

    while True:
        command = str(input('''
            ¿Qué deseas hacer?

            [p]render
            [a]pagar
            [s]alir
        '''))

        if command == 'p':
            lamp.turn_on()
        elif command == 'a':
            lamp.turn_off()
        elif command == 's':
            break
        else:
            print('\nIngresa un comando válido!')
            time.sleep(1)
            os.system('cls')


if __name__ == '__main__':
    run()
