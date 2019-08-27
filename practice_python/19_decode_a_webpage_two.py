import requests
from bs4 import BeautifulSoup

# Using the requests and BeautifulSoup Python libraries, print to the screen the full text of the article on this website: http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.

# The article is long, so it is split up between 4 pages.
# Your task is to print out the text to the screen so that you can read the full article without having to click any buttons.

# This will just print the full text of the article to the screen.
# It will not make it easy to read, so next exercise we will learn how to write this text to a .txt file.


def run():
    URL = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
    response = requests.get(URL).text
    soup = BeautifulSoup(response, 'html.parser')
    text = []

    # Construcción de una lista con todos los párrafos del artículo
    for element in soup.find_all('p'):
        text.append(element.text)

    for idx, p in enumerate(text):  # Impresión de párrafos necesarios
        if(idx <= 3 or idx >= len(text) - 4):
            continue
        print('\n' + p)


if __name__ == '__main__':
    run()
