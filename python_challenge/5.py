# URL = http://www.pythonchallenge.com/pc/def/peak.html
import pickle


def run():
    text = 'yes! pickle!'
    with open('5_text_unix.pickle', 'rb') as f:
        decoded_text = pickle.load(f)
    print(decoded_text)
    for line in decoded_text:
        for group in line:
            for i in range(group[1]):
                print(group[0], end='')
        print('\n')


if __name__ == '__main__':
    run()
