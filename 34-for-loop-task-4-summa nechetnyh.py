n = int(input())
result = 0
for i in range(n):
    number = int(input())
    if number % 2 == 1:
        result += number
print(f"Result = {result}")