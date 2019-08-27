# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list.
# For practice, write this code inside a function.


def first_and_last_element_of_a_list(number_list):
    if(len(number_list) <= 1):
        return number_list
    return [number_list[0], number_list[len(number_list) - 1]]


def run():
    a = [5, 10, 15, 20, 25]
    b = [2]
    c = []
    d = [2, 3]
    print(first_and_last_element_of_a_list(a))


if __name__ == '__main__':
    run()
