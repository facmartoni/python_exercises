import random

# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

# Extras:

# Write two different functions to do this - one using a loop and constructing a list, and another using sets.
# Go back and do Exercise 5 using sets, and write the solution for that in a different function.


def unique_elements_with_loop(number_list):
    unique_elements = []
    for number in number_list:
        if number not in unique_elements:
            unique_elements.append(number)
    return unique_elements


def unique_elements_with_sets(number_list):
    return list(set(number_list))


def run():
    population = range(random.randint(1, 50))
    a = random.sample(population, random.randint(1, len(population)))
    print(f'Original list: {a}')
    print(
        f'Unique elements with a loop: {sorted(unique_elements_with_loop(a))}')
    print(
        f'Unique elements with a set: {sorted(unique_elements_with_sets(a))}')


if __name__ == '__main__':
    run()
