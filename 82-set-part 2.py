'''
Множество
Set
'''
numbers = [i for i in range(1, 11)]
'''
то же самое что написать:
numbers = []
for i in range(1, 11):
    numbers.append(i)
'''
numbers.append(5)
print(numbers)
my_set = set(numbers)
print(my_set)
my_set.remove((1))
print(my_set)
for value in my_set:
    print(value)
