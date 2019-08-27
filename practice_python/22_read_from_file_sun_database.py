# Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file, and print out the results to the screen.

# Extra:

# Instead of using the .txt file from above (or instead of, if you want the challenge), take this .txt file, and count how many of each “category” of each image there are.
# This text file is actually a list of files corresponding to the SUN database scene recognition database, and lists the file directory hierarchy for the images.
# Once you take a look at the first line or two of the file, it will be clear which part represents the scene category.
# To do this, you’re going to have to remember a bit about string parsing in Python 3.


def run():
    categories = {}

    with open('categories.txt', 'r') as f:
        line = f.readline()
        while line:

            category = line.split('/')[2]

            if category not in categories:
                categories[category] = 1
            else:
                categories[category] += 1

            line = f.readline()

    print(categories)


if __name__ == '__main__':
    run()
