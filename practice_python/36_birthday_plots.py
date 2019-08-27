import bokeh.plotting
import collections
import json

# This exercise is Part 4 of 4 of the birthday data exercise series.

# In the previous exercise we counted how many birthdays there are in each month in our dictionary of birthdays.

# In this exercise, use the bokeh Python library to plot a histogram of which months the scientists have birthdays in!
# Because it would take a long time for you to input the months of various scientists, you can use my scientist birthday JSON file.
# Just parse out the months (if you don’t know how, I suggest looking at the previous exercise or its solution) and draw your histogram.

# If you are using a purely web-based interface for coding, this exercise won’t work for you, since it requires installing the bokeh Python package.
# Now might be a good time to install Python on your own computer.

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

    months_name = list(months.keys())
    months_quantity = list(months.values())

    # print(months_name)
    # print(months_quantity)

    bokeh.plotting.output_file('plot.html')
    plot = bokeh.plotting.figure(x_range=list(MONTHS.values()))
    plot.vbar(x=months_name, top=months_quantity, width=0.7)
    bokeh.plotting.show(plot)


if __name__ == '__main__':
    run()
