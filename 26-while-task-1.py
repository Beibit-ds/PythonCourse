zagadannoe_chislo = 5
guess = 0
popytka = 0
while zagadannoe_chislo != guess and popytka < 3:
    guess = int(input("Guess: "))
    popytka += 1