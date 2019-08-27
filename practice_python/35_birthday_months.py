import collections
import json

# This exercise is Part 3 of 4 of the birthday data exercise series.

# In the previous exercise we saved information about famous scientists’ names and birthdays to disk.
# In this exercise, load that JSON file from disk, extract the months of all the birthdays, and count how many scientists have a birthday in each month.

# Your program should output something like:

# {
# 	"May": 3,
# 	"November": 2,
# 	"December": 1
# }

MONTHS = {
    '1': 'January',
    '2': 'February',
    '3': 'March',
    '4': 'April',
    '5': 'May',
    '6': 'June',
    '7': 'July',
    '8': 'August',
    '9': 'September',
    '10': 'October',
    '11': 'November',
    '12': 'December'
}


def run():
    try:
        with open('birthdays.json', 'r') as f:
            birthdays = json.load(f).values()
    except:
        print('The "birthdays.json" file does not exist')
        exit()

    months = []
    for birthday in birthdays:
        birthday = birthday.split('/')
        month = str(int(birthday[1]))
        months.append(MONTHS[month])

    months = collections.Counter(months)
    print(months)


if __name__ == '__main__':
    run()
