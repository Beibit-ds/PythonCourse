import random

pravilno = 0
nepravilno = 0
while True:
    number_1 = random.randint(0, 10)
    number_2 = random.randint(0, 10)
    print(f"{number_1} + {number_2} = ", end="")
    answer = int(input())
    if answer == number_1 + number_2:
        print("Yes")
        pravilno += 1
    else:
        print("No")
        nepravilno += 1
    if nepravilno == 3:
        break
print(f"Game over. Your score: {pravilno}")

