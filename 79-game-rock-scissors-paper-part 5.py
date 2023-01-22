import random

options = {
    0: "rock",
    1: "scissors",
    2: "paper"
}
cases = {
    (0, 1): 1,
    (0, 2): 2,
    (1, 0): 2,
    (1, 2): 1,
    (2, 0): 1,
    (2, 1): 2
}
player_1, player_2 = 0, 0
count_1, count_2 = 0, 0
while count_1 < 3 and count_2 < 3:
    player_1 = random.randint(0,2)
    player_2 = random.randint(0,2)
    print(f"Player 1 selected: {player_1, options[player_1]}")
    print(f"Player 2 selected: {player_2, options[player_2]}")
    if player_1 != player_2:
        if cases[(player_1, player_2)] == 1:
            count_1 += 1
        else:
            count_2 += 1
        print(f"Player { cases[(player_1, player_2)]} won this round!")
    else:
        print("Draw!")
print(f"Player 1: { count_1 }")
print(f"Player 2: { count_2 }")
if count_1 == 3: print("Player 1 won!")
else: print("Player 2 won!")