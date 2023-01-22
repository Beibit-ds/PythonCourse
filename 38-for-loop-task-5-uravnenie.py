# x**x + 2*x + 3*x*y + 5 = N
N = int(input())
found = False
for x in range(-100, 101):
    for y in range(-100, 101):
        if x**x + 2*x + 3*x*y + 5 == N:
            print(x, y)
            found = True
if not found:
    print("Not found in the range")