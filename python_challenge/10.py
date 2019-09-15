# URL = http://www.pythonchallenge.com/pc/return/bull.html

# sequence = a = [1, 11, 21, 1211, 111221]
# len(sequence[num]) = [1, 2, 2, 4, 6, 12, 22, 44]


def run():
    a = ['1']
    count = 1
    while len(a) <= 30:
        element = f'{a[-1]}-'
        next_element = ''
        count = 1
        for idx, num in enumerate(element):
            if num == '-':
                count = 1
                break
            elif element[idx + 1] == num:
                count += 1
                continue
            else:
                next_element += f'{str(count)}{num}'
                count = 1
        a.append(next_element)
    print(len(a[30]))


if __name__ == '__main__':
    run()

# multiplier = 1
    # while(len(lenght) <= 30):
    #     multiplier *= 2
    #     lenght.append(lenght[-2] + multiplier)

    # while(len(lenght) <= 30):
    #     lenght.append(lenght[-1] + lenght[-2])

    # while len(string_chain) <= 30:
    #     element = f'-{string_chain[-1][::-1]}-'
    #     next_element = ''
    #     added_11 = False

    #     for idx, num in enumerate(element):
    #         if added_11:
    #             added_11 = False
    #             continue
    #         if element[idx] == '1' and element[idx + 1] == '1':
    #             # next_element += '21'
    #             next_element = '21' + next_element
    #             added_11 = True
    #             continue
    #         if element[idx] == '2':
    #             # next_element += '12'
    #             next_element = '12' + next_element
    #             continue
    #         if element[idx] == '1' and element[idx + 1] != '1' and not added_11:
    #             # next_element += '11'
    #             next_element = '11' + next_element
    #             continue
    #     string_chain.append(next_element)

    # print(string_chain[:7])
    # print(len(string_chain[30]))
    # print(len(string_chain))

    # a = [1, 11, 21, 1211, 111221]
    # two_prime_divisors = []
    # number = 1
    # while True:
    #     divisors = [divisor for divisor in range(
    #         1, number + 1) if number % divisor == 0]
    #     if len(divisors[1:-1]) == 2:
    #         if is_prime(divisors[1]) and is_prime(divisors[2]) and divisors[1] * divisors[2] == number:
    #             two_prime_divisors.append(number)
    #             print(number)
    #     number += 1
