# mini-calculator
number_1 = int(input())
number_2 = int(input())
operator = input()
if operator == '+':
    print(f"{number_1}{operator}{number_2} = {number_1 + number_2}")
elif operator == '-':
    print(f"{number_1}{operator}{number_2} = {number_1 - number_2}")
elif operator == '*':
    print(f"{number_1}{operator}{number_2} = {number_1 * number_2}")
elif operator == '/':
    if number_2 != 0:
        print(f"{number_1}{operator}{number_2} = {number_1 / number_2}")
    else:
        print("Деление на 0")
else:
    print("Ошибка")