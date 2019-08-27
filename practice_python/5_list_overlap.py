import random

# Take two lists, say for example these two:

#  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

# Extras:

# Randomly generate two lists to test this
# Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)


def run():
    a = random.sample(range(1, 50), random.randint(1, 20))
    b = random.sample(range(1, 50), random.randint(1, 20))

    # a = [num for num in range(0, random.randint(1, 100))
    #      if num % random.randint(1, 10) == 0]
    # b = [num for num in range(0, random.randint(1, 100))
    #      if num % random.randint(1, 10) == 0]

    print(a, b)
    print(
        f'The intersection of the lists is {list(set(a).intersection(set(b)))}')


if __name__ == '__main__':
    run()
