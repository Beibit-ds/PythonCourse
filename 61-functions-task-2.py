def calculate(num1, num2, operator='+'):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2

num_1 = int(input())
num_2 = int(input())
operator = input()
result = calculate(num_1, num_2, operator)
print(result)