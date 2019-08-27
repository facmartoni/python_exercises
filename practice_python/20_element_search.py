
def binary_search(ordered_list, number, min_idx, max_idx):

    mid_idx = (max_idx + min_idx) // 2

    if min_idx > max_idx:
        return False

    if ordered_list[mid_idx] == number:
        return True
    elif ordered_list[mid_idx] > number:
        return binary_search(ordered_list, number, min_idx, mid_idx - 1)
    else:
        return binary_search(ordered_list, number, mid_idx + 1, max_idx)


def run():

    # Sample list
    a = [1, 3, 7, 3, 7, 5, 8, 9, 10, 46, 73, 556, 86, 2, 1, 34]

    # Number to search in the list
    number = int(input('Give me a number: '))

    print('\n')
    print(sorted(a))
    if(binary_search(sorted(a), number, 0, len(a) - 1)):
        print(f'\nThe number {number} is in the list')
    else:
        print(f'\nThe number {number} isn\'t in the list')


if __name__ == '__main__':
    run()
