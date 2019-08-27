
def is_palindrome2(word):
    reversed_word = word[::-1]
    if reversed_word == word:
        return True
    else:
        return False


def is_palindrome(word):
    reversed_letters = []
    for letter in word:
        reversed_letters.insert(0, letter)

    reversed_word = ''.join(reversed_letters)

    if reversed_word == word:
        return True
    else:
        return False


def run():
    word = str(input('Escribe una palabra: '))
    if(is_palindrome2(word)):
        print(f'{word} ES PALINDROMO')
    else:
        print(f'{word} NO ES PALINDROMO')


if __name__ == '__main__':
    run()
