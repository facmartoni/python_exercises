import requests
from bs4 import BeautifulSoup

# Take the code from the How To Decode A Website exercise (if you didn’t do it or just want to play with some different code, use the code from the solution), and instead of printing the results to a screen, write the results to a txt file.
# In your code, just make up a name for the file you are saving to.

# Extras:

# Ask the user to specify the name of the output file that will be saved.

URL = 'https://www.nytimes.com/'


def get_nyt_titles():
    response = requests.get(URL).text
    soup = BeautifulSoup(response, 'html.parser')
    titles = soup.find_all('h2')
    titles = [element.get_text() for element in titles]
    return titles[:-2]


def write_titles_to_a_file(text_list, filename):
    with open(f'{filename}.txt', 'w') as f:
        for element in text_list:
            f.write(element + '\n\n')


def run():
    titles = get_nyt_titles()

    filename = input('Give me a filename to save the NYT titles: ')

    print('\nGenerating the file...')
    write_titles_to_a_file(titles, filename)

    input('\nPress enter to quit...')


if __name__ == "__main__":
    run()
