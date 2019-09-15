# URL = http://www.pythonchallenge.com/pc/def/equality.html

import re
import collections


def run():
    with open('3_text.txt', 'r') as f:
        text = f.read()

    patterns = re.findall(
        r'[a-z][A-Z][A-Z][A-Z][a-z][A-Z][A-Z][A-Z][a-z]', text)
    print(patterns)

    # print(collections.Counter(list(text)))


if __name__ == '__main__':
    run()
