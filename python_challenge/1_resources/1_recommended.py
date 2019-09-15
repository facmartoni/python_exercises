# URL = http://www.pythonchallenge.com/pc/def/map.html


def run():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet_mod = "cdefghijklmnopqrstuvwxyzab"
    mapping = str.maketrans(alphabet, alphabet_mod)

    text = input('Text: ')
    print(text.translate(mapping))


if __name__ == '__main__':
    run()
