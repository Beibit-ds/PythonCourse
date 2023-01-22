def find_minimum_with_sort(numbers):
    numbers.sort()
    return numbers[0]

def find_minimum_in_list(numbers):
    minimum = numbers[0]
    for number in numbers:
        if number < minimum:
            minimum = number
    return  minimum

numbers = [2,4,56,123,-123,0]
print(find_minimum_in_list(numbers))
print(numbers)
print(find_minimum_with_sort(numbers))
print(numbers)