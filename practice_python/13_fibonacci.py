# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
# Take this opportunity to think about how you can use functions.
# Make sure to ask the user to enter the number of numbers in the sequence to generate.
# (Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence.
# The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)


def fibonacci_generator_without_recursion(number_of_fibonacci_numbers):
    if number_of_fibonacci_numbers == 1:
        return [1]
    if number_of_fibonacci_numbers == 2:
        return [1, 1]
    fibonacci_list = [1, 1]
    for i in range(3, number_of_fibonacci_numbers + 1):
        fibonacci_list.append(fibonacci_list[len(
            fibonacci_list) - 1] + fibonacci_list[len(fibonacci_list) - 2])
    return fibonacci_list


def fibonacci_generator(number_of_fibonacci_numbers):
    if number_of_fibonacci_numbers == 1:
        return [1]
    if number_of_fibonacci_numbers == 2:
        return [1, 1]
    fibonacci_list = [1, 1]
    for i in range(3, number_of_fibonacci_numbers + 1):
        fibonacci_list.append(fibonacci_element(i))
    return fibonacci_list


def fibonacci_element(number_element):
    if number_element == 1:
        return 1
    if number_element == 2:
        return 1
    return fibonacci_element(number_element - 1) + fibonacci_element(number_element - 2)


def run():
    number_of_fibonacci_numbers = int(
        input('Enter the number of fibonacci numbers you want: '))
    print(fibonacci_generator_without_recursion(number_of_fibonacci_numbers))


if __name__ == '__main__':
    run()
