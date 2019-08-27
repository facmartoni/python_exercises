
def run():
    count = 1
    while(True):
        try:
            num1 = str(input())
            num2 = str(input())
            subsequences = num2.count(num1)
            last_subsequence_index = num2.rfind(num1) + 1
            print(f'Caso #{count}:')
            if(subsequences != 0):
                print(f'Qtd.Subsequencias: {subsequences}')
                print(f'Pos: {last_subsequence_index}')
            else:
                print('Nao existe subsequencia')
            print('')
            count += 1
        except EOFError:
            break


if __name__ == '__main__':
    run()
