# y = 25 + x -> x = y - 25
y = int(input())
found = False
for x in range(-100, 101):
    if y == 25 + x:
        found = True
        print(f"X = {x}")
        break
if not found:
    print("I couldn't find corresponding X in range -100 .. 100")