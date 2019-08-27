"""
"abacabad" c
"abacabaabacaba" _
"abcdefghijklmnopqrstuvwxyziflskecznslkjfabe" d
"bcccccccccccccyb" y
"""


def first_not_repeating_char(char_sequence):
    char_list = []
    letters_banned = []
    for letter in char_sequence:
        if letter not in char_list and letter not in letters_banned:
            char_list.append(letter)
        else:
            if(letter in char_list):
                char_list.remove(letter)
            letters_banned.append(letter)
    if(len(char_list) == 0):
        return '_'
    else:
        return char_list[0]


def run():
    char_sequence = str(input('Escribe una secuencia de caracteres: '))
    result = first_not_repeating_char(char_sequence)
    if(result == '_'):
        print('Todos los caracteres se repiten')
    else:
        print(f'El primer caracter no repetido es {result}')


if __name__ == '__main__':
    run()
