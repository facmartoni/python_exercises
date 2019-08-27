def change_is_possible(buy_price, paid_price):
    bills = [100, 50, 20, 10, 5, 2]
    difference = paid_price - buy_price
    count = 0

    for bill in bills:
        if(difference >= bill):
            difference -= bill
            count += 1
        if(count > 2):
            return False

    if(difference == 0 and count == 2):
        return True

    return False


def run():
    # buy_price = int(input())
    # paid_price = int(input())
    buy_price, paid_price = map(int, input().split())

    while(buy_price != 0 and paid_price != 0):

        if(change_is_possible(buy_price, paid_price)):
            print('possible')
        else:
            print('impossible')
        # buy_price = int(input())
        # paid_price = int(input())
        buy_price, paid_price = map(int, input().split())


if __name__ == '__main__':
    run()
