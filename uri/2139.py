from datetime import datetime


def run():
    while True:
        try:
            month, day = map(int, input().split())

            christmas_2016 = datetime(2016, 12, 25)
            actual_day = datetime(2016, month, day)
            difference = christmas_2016 - actual_day
            days_difference = difference.days

            if days_difference == 0:
                print('E natal!')
            elif days_difference == 1:
                print('E vespera de natal!')
            elif days_difference < 0:
                print('Ja passou!')
            else:
                print('Faltam %d dias para o natal!' % days_difference)

        except:
            break


if __name__ == '__main__':
    run()
