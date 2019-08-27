import random
import os

IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        ========='''
          ]

WORDS = [
    'perl',
    'python',
    'java',
    'javascript',
    'delphi',
    'go',
    'kotlin',
    'swift',
    'objectivec',
    'dart',
    'bash',
    'rust',
    'scala',
    'matlab',
    'haskell',
    'prolog',
    'pascal',
    'fortran',
    'vba',
    'php',
    'html',
    'css',
    'sql',
    'assembly',
    'ruby',
]


def random_word():
    # random_id = random.randint(0, len(WORDS) - 1)
    # return WORDS[random_id]
    return random.choice(WORDS)


def display_board(tries, hidden_word):
    # Esta instrucción solo funciona en Windows, la concha de su madre
    os.system('cls')
    print('J U E G O  D E L  A H O R C A D O  P A R A  P R O G R A M A D O R E S')
    print(IMAGES[tries])
    print(f'\n\n{hidden_word}')
    print('****************************')


def run():
    word = random_word()
    hidden_word = ['-'] * len(word)
    tries = 0

    while True:
        display_board(tries, hidden_word)
        current_input = str(input('Escribe una letra o palabra: '))
        letter_indexes = []

        if(len(current_input) == 1):

            for i in range(len(word)):
                if word[i] == current_input:
                    letter_indexes.append(i)

            if len(letter_indexes) == 0:
                tries += 1
            else:
                for i in letter_indexes:
                    hidden_word[i] = current_input

            if(tries == len(IMAGES) - 1):
                display_board(tries, hidden_word)
                print(
                    f'\n Lo sentimos, perdiste :(. La palabra correcta era {word}')
                break

            if(''.join(hidden_word) == word):
                display_board(tries, hidden_word)
                print('\n ¡Ganaste! Adivinaste la palabra')
                break
        else:

            if ''.join(current_input) == word:
                hidden_word = list(current_input)
                display_board(tries, hidden_word)
                print(
                    f'\n ¡Ganaste! Adivinaste la palabra, la misma era {current_input}')
                break

            else:
                tries += 1


if __name__ == '__main__':
    while True:
        run()
        decision = str(
            input('\n ¿Volver a jugar? Escribe "s". De lo contrario escribe "n": '))
        while True:
            if(decision == 's'):
                break
            elif(decision == 'n'):
                exit()
            else:
                decision = str(input('Escribe una opción válida: '))
                continue
