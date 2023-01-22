number_1 = int(input())
number_2 = int(input())
total = 0
if number_1 > number_2:
    number_1, number_2 = number_2, number_1
for number in range(number_1, number_2 + 1):
    total += number
print(f"Tota l = {total}")