def find_minimum_with_sort(numbers):
    numbers.sort()
    return numbers[0]

def find_minimum_in_list(numbers):
    minimum = numbers[0]
    for number in numbers:
        if number < minimum:
            minimum = number
    return  minimum


def find_max_in_list(numbers):
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    return  maximum
