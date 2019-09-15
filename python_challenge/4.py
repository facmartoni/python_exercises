# URL = http://www.pythonchallenge.com/pc/def/linkedlist.php
import requests
import re

URL = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='


def run():
    num = 46145
    i = 0
    while i < 500:
        print(i)
        print(num)
        response = requests.get(URL + str(num))
        content = str(response.content)
        match = re.search(r'[1-9][0-9]*', content)

        if not match:
            if re.search(r'Divide by two', content):
                num = num // 2
                i += 1
                continue
            else:
                print(num)
                break

        num = match.string[match.start():match.end()]
        i += 1


if __name__ == '__main__':
    run()

# Esto es increíblemente complejo
# The final num was 66831
