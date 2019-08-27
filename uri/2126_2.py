def quantity_of_subsequences(num1, num2):
    for_count = 0
    quantity = 0
    for letter in num2:
        if(for_count <= len(num2) - len(num1)):
            found = True
            if(letter == num1[0]):
                internal_for_count = for_count
                for letter in num1:
                    if(letter != num2[internal_for_count]):
                        found = False
                        break
                    internal_for_count += 1
                if found:
                    quantity += 1
            for_count += 1
        else:
            break
    return quantity


def run():
    count = 1
    while(True):
        try:
            num1 = str(input())
            num2 = str(input())
            # subsequences = num2.count(num1)
            subsequences = quantity_of_subsequences(num1, num2)
            last_subsequence_index = num2.rfind(num1) + 1

            print(f'Caso #{count}:')
            if(subsequences != 0):
                print(f'Qtd.Subsequencias: {subsequences}')
                print(f'Pos: {last_subsequence_index}')
            else:
                print('Nao existe subsequencia')
            print('')
            count += 1
        except:
            break


if __name__ == '__main__':
    run()
