# Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

#   My name is Michele
# Then I would see the string:

#   Michele is name My
# shown back to me.


def reverse_text(text):
    words_list = text.split()
    words_list = words_list[::-1]
    reversed_text = ' '.join(words_list)
    return reversed_text


def run():
    text = input('Give me some text: ')
    print(f'Here is the text reversed :)\n\n{reverse_text(text)}')


if __name__ == '__main__':
    run()
