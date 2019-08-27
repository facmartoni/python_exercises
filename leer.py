
def run():
    count = 0
    with open('aleph.txt') as f:
        for line in f:
            count += line.count('Beatriz')
    print(f'Beatriz se encuentra {count} veces en el texto')


if __name__ == '__main__':
    run()
