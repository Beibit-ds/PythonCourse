# 2*X + 5*Y = 32
found = False
for x in range(-100, 101):
    for y in range(-100, 101):
        if 2*x + 5*y == 32:
            print(x, y)
            found = True
if not found:
    print("Not found")