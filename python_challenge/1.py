# URL = http://www.pythonchallenge.com/pc/def/map.html

ALPHABET = {
    1: 'a',
    2: 'b',
    3: 'c',
    4: 'd',
    5: 'e',
    6: 'f',
    7: 'g',
    8: 'h',
    9: 'i',
    10: 'j',
    11: 'k',
    12: 'l',
    13: 'm',
    14: 'n',
    15: 'o',
    16: 'p',
    17: 'q',
    18: 'r',
    19: 's',
    20: 't',
    21: 'u',
    22: 'v',
    23: 'w',
    24: 'x',
    25: 'y',
    26: 'z',
    27: 'a',
    28: 'b',
}


def run():
    text = list(input('Text: '))

    positions_in_alphabet = []
    for letter in text:
        for key, value in ALPHABET.items():
            if value == letter:
                positions_in_alphabet.append(key)
                break
        else:
            positions_in_alphabet.append(letter)

    positions_in_alphabet_decoded = [
        num + 2 if type(num) == int else num for num in positions_in_alphabet]

    text_decoded = [ALPHABET[num] if num in ALPHABET
                    else num for num in positions_in_alphabet_decoded]

    text_decoded = ' '.join(text_decoded)
    print(text_decoded)


if __name__ == '__main__':
    run()
