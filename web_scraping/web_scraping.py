import requests
from bs4 import BeautifulSoup
import urllib.request

URL = 'https://xkcd.com/'


def run():
    for i in range(1, 6):
        response = requests.get(f'{URL}{i}')
        soup = BeautifulSoup(response.content, 'html.parser')
        image_container = soup.find(id='comic')
        image_url = image_container.find('img')['src']
        image_name = image_url.split('/')[-1]
        print(f'Descargando {image_name}')
        urllib.request.urlretrieve(f'https:{image_url}', image_name)


if __name__ == '__main__':
    run()
