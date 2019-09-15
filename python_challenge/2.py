# URL = http://www.pythonchallenge.com/pc/def/ocr.html

import collections


def run():
    with open('2_text.txt', 'r') as f:
        text = f.read()
    quantity_of_symbols = collections.Counter(text)
    print(quantity_of_symbols)


if __name__ == '__main__':
    run()
