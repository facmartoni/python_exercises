import os
import time

KEYS = {
    'a': 'w',
    'b': 'E',
    'c': 'x',
    'd': '1',
    'e': 'a',
    'f': 't',
    'g': '0',
    'h': 'C',
    'i': 'b',
    'j': '!',
    'k': 'z',
    'l': '8',
    'm': 'M',
    'n': 'I',
    'o': 'd',
    'p': '.',
    'q': 'U',
    'r': 'Y',
    's': 'i',
    't': '3',
    'u': ',',
    'v': 'J',
    'w': 'N',
    'x': 'f',
    'y': 'm',
    'z': 'W',
    'A': 'G',
    'B': 'S',
    'C': 'j',
    'D': 'n',
    'E': 's',
    'F': 'Q',
    'G': 'o',
    'H': 'e',
    'I': 'u',
    'J': 'g',
    'K': '2',
    'L': '9',
    'M': 'A',
    'N': '5',
    'O': '4',
    'P': '?',
    'Q': 'c',
    'R': 'r',
    'S': 'O',
    'T': 'P',
    'U': 'h',
    'V': '6',
    'W': 'q',
    'X': 'H',
    'Y': 'R',
    'Z': 'l',
    '0': 'k',
    '1': '7',
    '2': 'X',
    '3': 'L',
    '4': 'p',
    '5': 'v',
    '6': 'T',
    '7': 'V',
    '8': 'y',
    '9': 'K',
    '.': 'Z',
    ',': 'D',
    '?': 'F',
    '!': 'B',
}


def cipher(message):
    words = message.split(' ')
    cipher_message = []

    for word in words:
        cipher_word = ''
        for letter in word:
            if(letter not in KEYS):
                cipher_word += letter
            else:
                cipher_word += KEYS[letter]
        cipher_message.append(cipher_word)

    return ' '.join(cipher_message)


def decipher(message):
    words = message.split(' ')
    decipher_message = []

    for word in words:
        decipher_word = ''
        for letter in word:
            encountered = False
            for key, value in KEYS.items():
                if(letter == value):
                    decipher_word += key
                    encountered = True
                    break
            if(not encountered):
                decipher_word += letter
        decipher_message.append(decipher_word)

    return ' '.join(decipher_message)


def run():
    while True:
        os.system('cls')  # Solo funca en Windows :/
        command = str(input('''
        * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- *
        |      Bienvenido al programa de cifrado de Alan Turing     |
        * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- *

        [c]ifrar mensaje
        [d]ecifrar mensaje
        [s]alir

        Escribe una opción: '''))

        if(command == 'c'):
            message = str(input('\nEscribe tu mensaje: '))
            cipher_message = cipher(message)
            print('')
            print(cipher_message)
            return_to_menu = str(
                input('\n Para volver al menú presiona enter...'))
        elif(command == 'd'):
            message = str(input('\nEscribe tu mensaje cifrado: '))
            decipher_message = decipher(message)
            print('')
            print(decipher_message)
            return_to_menu = str(
                input('\n Para volver al menú presiona enter...'))
        elif(command == 's'):
            break
        else:
            print('\n Escribe una opción válida!')
            time.sleep(1)


if __name__ == '__main__':
    run()
