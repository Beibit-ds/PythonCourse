# option 1
numbers = [2,4,56,123,-123,0]
numbers.sort()
print(numbers[0])
# option 2
numbers = [2,4,56,123,-123,0]
minimum = numbers[0]
for number in numbers:
    if number < minimum:
        minimum = number
print(minimum)