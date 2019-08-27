# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)


def is_palindrome(string):
    if string == string[::-1]:
        return True
    return False


def run():
    string = input('Enter a text: ')
    if(is_palindrome(string)):
        print('This is a palindrome')
    else:
        print('This is not a palindrome')


if __name__ == '__main__':
    run()
