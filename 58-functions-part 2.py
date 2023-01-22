'''
Functions
y = kx + b
'''
def add_two_numbers(number_1, number_2=5):
    c = number_1 + number_2
    print(f"{number_1} + {number_2} = {c}")

a = int(input())
b = int(input())
add_two_numbers(number_1=a, number_2=b)
add_two_numbers(a)