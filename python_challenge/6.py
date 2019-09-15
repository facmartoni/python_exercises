# URL = http://www.pythonchallenge.com/pc/def/channel.html
import re
import zipfile


def search_in_files():
    filenames = []
    num = 90052
    filenames.append(num)
    for i in range(910):
        with open(f'./6_texts/{str(num)}.txt', 'r') as f:
            content = f.read()
        match = re.search(r'[1-9][0-9]*', content)
        match_text = re.search(r'Next nothing is', content)

        if not match_text:
            print(num + ' ' + content)
            break

        num = match.string[match.start():match.end()]
        filenames.append(num)
    return filenames


def run():
    filenames = search_in_files()
    channel_zip = zipfile.ZipFile(r'./6_texts/channel.zip', 'r')
    comments = []
    for filename in filenames:
        comments.append(str(channel_zip.getinfo(
            f'{filename}.txt').comment)[2:-1])
    for comment in comments:
        if comment == r'\n':
            print()
        else:
            print(comment, end='')


if __name__ == '__main__':
    run()
