import random
from dictionaries import options, cases

def select_and_print_selection(player):
    selection = random.randint(0, 2)
    print(f"Player {player} selected: {selection, options[selection]}")
    return selection

player_1, player_2 = 0, 0
count_1, count_2 = 0, 0
while count_1 < 3 and count_2 < 3:
    player_1 = select_and_print_selection(1)
    player_2 = select_and_print_selection(2)
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