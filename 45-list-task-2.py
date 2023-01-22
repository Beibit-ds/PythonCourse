n = int(input())
lst = []
for i in range(n):
    number = int(input())
    lst.append(number)
threshold = int(input())
for num in lst:
    if num < threshold:
        print(num)
