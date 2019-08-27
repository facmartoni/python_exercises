import os
import time
import textwrap

KEYS = {
    'a': '01110111',
    'b': '01000101',
    'c': '01111000',
    'd': '00110001',
    'e': '01100001',
    'f': '01110100',
    'g': '00110000',
    'h': '01000011',
    'i': '01100010',
    'j': '00100001',
    'k': '01111010',
    'l': '00111000',
    'm': '01001101',
    'n': '01001001',
    'o': '01100100',
    'p': '00101110',
    'q': '01010101',
    'r': '01011001',
    's': '01101001',
    't': '00110011',
    'u': '00101100',
    'v': '01001010',
    'w': '01001110',
    'x': '01100110',
    'y': '01101101',
    'z': '01010111',
    'A': '01000111',
    'B': '01010011',
    'C': '01101010',
    'D': '01101110',
    'E': '01110011',
    'F': '01010001',
    'G': '01101111',
    'H': '01100101',
    'I': '01110101',
    'J': '01100111',
    'K': '00110010',
    'L': '00111001',
    'M': '01000001',
    'N': '00110101',
    'O': '00110100',
    'P': '00111111',
    'Q': '01100011',
    'R': '01110010',
    'S': '01001111',
    'T': '01010000',
    'U': '01101000',
    'V': '00110110',
    'W': '01110001',
    'X': '01001000',
    'Y': '01010010',
    'Z': '01101100',
    '0': '01101011',
    '1': '00110111',
    '2': '01011000',
    '3': '01001100',
    '4': '01110000',
    '5': '01110110',
    '6': '01010100',
    '7': '01010110',
    '8': '01111001',
    '9': '01001011',
    '.': '01011010',
    ',': '01000100',
    '?': '01000110',
    '!': '01000010',
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
        word = textwrap.wrap(word, 8)
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
