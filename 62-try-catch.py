def calculate(num1, num2, operator='+'):
    try:
        num1 = int(num1)
        num2 = int(num2)
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            return num1 / num2
    except ZeroDivisionError:
        print("Be careful with zeroes.")
    except ValueError:
        print("Wrong value.")

num_1 = input()
num_2 = input()
operator = input()
result = calculate(num_1, num_2, operator)
print(result)